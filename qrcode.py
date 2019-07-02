#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import os, signal, subprocess
def paizhao():
    os.system("raspistill -w 320 -h 240 -t 5000 -tl 1000 -o /home/pi/image%02d.jpg")
def chuli():
    tt = 0
    while tt < 6 :
        ttm='%02d' %tt
        str1 = "zbarimg --raw /home/pi/image"+ttm+".jpg"
        str2 = "image"+ttm+".jpg"
        if(os.path.isfile(str2)):
            zbarcam=subprocess.Popen(str1, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
            qrcodetext=zbarcam.stdout.readline()
            if qrcodetext!="":
                with open('1.txt','a') as f:
                    f.write(qrcodetext)
                os.remove(str2)
            else:
                os.remove(str2)
            tt = tt + 1
            output=[]
            with open('1.txt') as fp:
                lines=fp.readlines()
                for i in lines:
                    if i not in output:
                        output.append(i)
            with open('2.txt','w') as fp1:
                for i in output:
                    fp1.write(i)

