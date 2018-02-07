
#!/usr/bin/env python3

import json
import os


filePath = './down/209_1479983924.zip_files/answers.json'  

def check(file_name,homeId):
    word = 0
    sentence = 0
    other = 0
    if os.path.exists('./unzip/'+file_name):
        filePath = './unzip/'+file_name+'/answers.json'
        dicPath = './unzip/'+file_name+'/answers.dic'
        if not os.path.exists(filePath):
            return
        mapFile = ''
        picFile = ''
        with open(filePath, encoding='utf-8') as f:
            pkList = json.load(f)
            #print(type(pkList))
            for pkData in pkList:
               #print(pkData)
               #print(pkData['type'])
               pktype = pkData['type']
               if pktype == '1':
                  word += 1
               elif pktype == '2':
                  sentence += 1
               else:
                  other += 1
               isMap3 = str(os.path.exists('./unzip/'+file_name+'/'+str(pkData['voice'])));
               isPic = str(os.path.exists('./unzip/'+file_name+'/'+str(pkData['pic'])));
               mapFile += str(pkData['voice'])+'='+isMap3+'\n'
               picFile += str(pkData['pic'])+'='+isPic+'\n'
        isexists = os.path.exists(filePath)
        isDic = os.path.exists(dicPath)
    
        strs = homeId+'\n'+file_name+'\n word='+str(word)+'  sentence='+str(sentence)+' other='+str(other)+' json='+str(isexists)+' dic='+str(isDic)+'\n'+mapFile+'\n'+picFile+'\n\n'
        print(strs)
        with open('test.txt', 'a',encoding='utf-8') as ff:
            ff.write(strs)

with open('allhomework.txt', encoding='utf-8') as f:
    urls = json.load(f)
    #print(urls)
    for url in urls:
       package_path = url['package_path']
       homeId = url['id']
       file_name = package_path.split('/')[-1]
       #print(file_name)
       if str(file_name):
           fileName = file_name.split('.')[0]
           check(fileName,homeId)








