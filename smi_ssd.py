import ujson as json
import requests

with open('Flash.SET','r') as f:
    data = f.readlines()

vendor = {
    'M': ['Micron','micron','MT'],
    'T': ['Toshiba','kioxia',['TH','TC']],
    'WD': ['Sandisk','westerndigital',''],
    'Y': ['YMTC','ymtc','YM'],
    'H': ['Hynix','skhynix','H5'],
    'S': ['Samsung','samsung','K9']
}

# target_vendor = 'M'

flash_list = {}

controller = ''

with open('.\\fdb.json','r',encoding='utf-8') as f:
    fdb = json.load(f)

n = 0

url = 'http://fe.barryblueice.cn/ID?param='

for h in list(vendor.keys())[::1]:
    target_vendor = h
    for i in data[::1]:
        if (vendor[target_vendor][0]) in i:
            n+=1
            if n % 2 == 0:
                i = i.split('=')
                flash_info_list = i[0]
                flash_id_list = i[-1]
                
                flash_info_list = flash_info_list.split(',')
                flash_id_list = flash_id_list.split(',')
                if len(flash_info_list) == 3:
                    flash_info = flash_info_list[-1]
                    if controller == '':
                        controller = flash_info[flash_info.find('SM'):flash_info.find(')',-1)]
                    elif controller == 'SM2259XT':
                        controller = 'SM2259XT2'
                else:
                    flash_info = flash_info_list[2]
                    if controller == '':
                        controller = (flash_info_list[-1])[flash_info_list[-1].find('SM'):flash_info_list[-1].find(')',-1)]
                    elif controller == 'SM2259XT':
                        controller = 'SM2259XT2'
                flash_info = flash_info[:flash_info.find('(',1)]

                m = 0
                flash_id = ''

                for j in flash_id_list:

                    m += 1

                    flash_id += j

                    if m == 6:
                        break

                try:
                    response = requests.get(url+flash_id).json()
                    process = response['process']
                
                except:

                    process = 'Unknown'

                try:

                    fdb["iddb"][flash_id]['n'].append(f"{(vendor[target_vendor][1])} {flash_info}")
                    fdb["iddb"][flash_id]['n'] = list(set(fdb["iddb"][flash_id]['n']))

                except:

                    fdb["iddb"].update({
                        flash_id : {
                            "n": [
                                f"{vendor[target_vendor][1]} {flash_info}"
                            ]
                        }
                    })

                if flash_id.startswith('EC'):
                    iscer = (requests.get("http://fe.barryblueice.cn/samsung-cer?param=" + flash_id).json())

                try:

                    if 'id' in list(fdb[vendor[target_vendor][1]][flash_info].keys()):
                        fdb[vendor[target_vendor][1]][flash_info]['id'].append(flash_id)
                        fdb[vendor[target_vendor][1]][flash_info]['id'] = list(set(fdb[vendor[target_vendor][1]][flash_info]['id']))
                    else:
                        fdb[vendor[target_vendor][1]][flash_info].update(
                            {'id':[flash_id]}
                        )

                except:

                    fdb[vendor[target_vendor][1]].update(
                            {flash_info:{'id':[flash_id]}}
                        )

                if 'l' in list(fdb[vendor[target_vendor][1]][flash_info].keys()):
                    if flash_id.startswith('EC'):
                        if iscer["result"] == True:
                            if not "CER" in fdb[vendor[target_vendor][1]][flash_info]['l']:
                                fdb[vendor[target_vendor][1]][flash_info]['l'] += ' CER'
                else:
                    if flash_id.startswith('EC'):
                        if iscer["result"] == True:
                            process += ' CER'

                    fdb[vendor[target_vendor][1]].update({flash_info:{}})
                    fdb[vendor[target_vendor][1]][flash_info].update({
                        'l': process
                    })


                # try:
                #     if flash_id.startswith('EC'):
                #         if iscer["result"] == True:
                #             if not "CER" in fdb[vendor[target_vendor][1]][flash_info]['l']:
                #                 fdb[vendor[target_vendor][1]][flash_info]['l'] += ' CER'
                #     else:
                #         fdb[vendor[target_vendor][1]][flash_info]['l'] = fdb[vendor[target_vendor][1]][flash_info]['l']
                # except:
                    
                #     try:
                #         if iscer["result"] == True:
                #             process += ' CER'
                #     except:
                #         pass
                    
                #     fdb[vendor[target_vendor][1]].update({flash_info:{}})
                #     fdb[vendor[target_vendor][1]][flash_info].update({
                #         'l': process
                #     })

                if 't' in list(fdb[vendor[target_vendor][1]][flash_info].keys()):
                    fdb[vendor[target_vendor][1]][flash_info]['t'].append(controller)
                    fdb[vendor[target_vendor][1]][flash_info]['t'] = list(set(fdb[vendor[target_vendor][1]][flash_info]['t']))
                else:
                    fdb[vendor[target_vendor][1]][flash_info].update({
                            't':[controller]
                    })
                
                
                # print()
                # print (flash_info)
                # print (flash_info_list)
                # print(f"{flash_id}")
                print (f'{flash_info} {flash_id} {controller} {process}')

with open('.\\fdb_new.json','w') as f:
    json.dump(fdb,f,indent=4,ensure_ascii=False)