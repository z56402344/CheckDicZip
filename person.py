
#!/usr/bin/env python3

class Person:
    def __init__(self, pkid, pktype, cn, pic, voice):
        self.id = pkid
        self.type = pktype
        self.cn = cn
        self.pic = pic
        self.voice = voice

    def work(self):
        print(self.name, 'is working...')
