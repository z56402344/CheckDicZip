
#!/usr/bin/env python3

import threading as thd
import time

def fn():
    print(time.time())
    thd.Timer(3,un_zip,(file_name,)).start()

#threading.Timer(延迟时间，函数名称，函数参数).start()
