
#!/usr/bin/env python3

import zipfile
import os
import json

def un_zip(file_name):
    unzipPath = './down/'+file_name
    if os.path.exists(unzipPath):
        zip_file = zipfile.ZipFile(unzipPath)
        fileName = file_name.split('.')[0]
        fileName = './unzip/'+fileName  
        if os.path.isdir(fileName):
            pass
        else:
            os.mkdir(fileName)
        for names in zip_file.namelist():
            zip_file.extract(names, fileName)
        zip_file.close()

with open('allhomework.txt', encoding='utf-8') as f:
    urls = json.load(f)
    print(urls)
    for url in urls:
       package_path = url['package_path']
       file_name = package_path.split('/')[-1]
       #print(file_name)
       if str(file_name):	
           un_zip(file_name)
