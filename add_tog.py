import ujson as json

with open('.\\fdb.json','r',encoding='utf-8') as f:
    data = json.load(f)

vendor = {
    'M': ['Micron','micron','MT'],
    'T': ['Toshiba','kioxia',['TH','TC']],
    'WD': ['Sandisk','westerndigital',''],
    'Y': ['YMTC','ymtc','YM'],
    'H': ['Hynix','skhynix','H5'],
    'S': ['Samsung','samsung','K9']
}

n = 0

for i in data['iddb']:
    try:
        match i[:2]:
            # case 'EC':
            #     for j in data['iddb'][i]['n']:
            #         if not str(j).startswith('samsung'):
            #             data['iddb'][i]['n'].remove(j)
            #             print (f'error: {j} (Expected: {i[:2]})')
            #             n+=1

            case '98':
                if len(i) == 12:
                    # print (i[-4:])
                    if i[-4:].isdecimal():
                        for j in data['iddb'][i]['n']:
                            part = j.replace('kioxia ','')
                            try:
                                data['kioxia'][part]['l'] += ' Toggle'
                            except:
                                pass

            case '45':

                if i[-4:].isdecimal():
                    # print('Toggle')
                    for j in data['iddb'][i]['n']:
                            part = j.replace('westerndigital ','')
                            try:
                                data['westerndigital'][part]['l'] += ' Toggle'
                            except:
                                pass

            case 'AD':
                if len(i) == 12:
                    if i[-1] == '0':
                        part = j.replace('skhynix ','')
                        try:
                            data['skhynix'][part]['l'] += ' Toggle'
                        except:
                            pass
                        # print('Toggle')
            case _:
                pass

    except:
        print (i)

with open('.\\fdb_new.json','w') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)