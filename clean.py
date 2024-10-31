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
            case 'EC':
                for j in data['iddb'][i]['n'][::-1]:
                    if not str(j).startswith('samsung'):
                        data['iddb'][i]['n'].remove(j)
                        # print (f'error: {j} (Expected: {i[:2]})')
                        n+=1

            case '2C':
                for j in data['iddb'][i]['n'][::-1]:
                    if not str(j).startswith('micron'):
                        data['iddb'][i]['n'].remove(j)
                        # print (f'error: {j} (Expected: {i[:2]})')
                        n+=1

            case '98':
                for j in data['iddb'][i]['n'][::-1]:
                    if not str(j).startswith('kioxia'):
                        data['iddb'][i]['n'].remove(j)
                        # print (f'error: {j} (Expected: {i[:2]})')
                        n+=1

            case '45':
                for j in data['iddb'][i]['n'][::-1]:
                    if not str(j).startswith('westerndigital'):
                        data['iddb'][i]['n'].remove(j)
                        # print (f'error: {j} (Expected: {i[:2]})')
                        n+=1
            
            case '9B':
                for j in data['iddb'][i]['n'][::-1]:
                    if not str(j).startswith('ymtc'):
                        data['iddb'][i]['n'].remove(j)
                        # print (f'error: {j} (Expected: {i[:2]})')
                        n+=1

            case 'AD':
                for j in data['iddb'][i]['n'][::-1]:
                    if not str(j).startswith('skhynix'):
                        data['iddb'][i]['n'].remove(j)
                        # print (f'error: {j} (Expected: {i[:2]})')
                        n+=1
            
            case _:
                pass

    except:
        pass

print(f'ID error: {n}')

n = 0

for i in data:
        
    try:

        match i:

            case 'intel':
                for j in data[i]:
                    for k in data[i][j]["id"][::-1]:
                        if not k.startswith('89'):
                            n += 1
                            k = data[i][j]["id"].index(k)
                            data[i][j]["id"].pop(k)

            case 'micron':
                for j in data[i]:
                    for k in data[i][j]["id"][::-1]:
                        if not k.startswith('2C') or k.startswith('B5'):
                            n += 1
                            data[i][j]["id"].remove(k)

            case 'kioxia':
                for j in data[i]:
                    for k in data[i][j]["id"][::-1]:
                        if not k.startswith('98'):
                            n += 1
                            data[i][j]["id"].remove(k)

            case 'westerndigital':
                for j in data[i]:
                    for k in data[i][j]["id"][::-1]:
                        if not k.startswith('45'):
                            n += 1
                            data[i][j]["id"].remove(k)

            case 'ymtc':
                for j in data[i]:
                    for k in data[i][j]["id"][::-1]:
                        if not k.startswith('9B'):
                            n += 1
                            data[i][j]["id"].remove(k)

            case 'skhynix':
                for j in data[i]:
                    for k in data[i][j]["id"][::-1]:
                        if not k.startswith('AD'):
                            n += 1
                            data[i][j]["id"].remove(k)

            case 'samsung':
                for j in data[i]:
                    for k in data[i][j]["id"][::-1]:
                        if not k.startswith('EC'):
                            n += 1
                            data[i][j]["id"].remove(k)

            case _:
                pass

    except:

        pass

print(f'PN error: {n}')

with open('.\\fdb_new.json','w') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)