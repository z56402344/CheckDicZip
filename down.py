
#!/usr/bin/env python3

import zipfile
import os
import urllib
import urllib.request
import threading as thd
import time
import json

file_name = '111.zip'

def Schedule(a,b,c):
    '''''  a:已经下载的数据块 b:数据块的大小 c:远程文件的大小 '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
        #with open('allzip.txt', 'a',encoding='utf-8') as ff:
            #ff.write(file_name.split('.')[0])
    print('%.2f%%' % per)

with open('allhomework.txt', encoding='utf-8') as f:
    urls = json.load(f)
    print(urls)
    for url in urls:
       package_path = url['package_path']
       if str(package_path):
           file_name = package_path.split('/')[-1]
           print(file_name)
           local = os.path.join('/work/check/down',str(file_name))
           try:
               urllib.request.urlretrieve(package_path,local,Schedule)
           except Exception as e:
               print(file_name+'  '+str(e))

#url = 'https://www.python.org/ftp/python/2.7.5/python-2.7.5-pdb.zip'
#local = url.split('/')[-1]
#local = os.path.join('/Users/Du/python',file_name)







