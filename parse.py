#-*- coding:utf-8 -*-
import numpy as np
import re
import time
def converttime(str):
    if str:#12/Feb/2014:03:08:11 +0800
        return time.strftime('%Y%m%d %H:%M:%S',time.strptime(str[:-6],'%d/%b/%Y:%H:%M:%S'))
#print converttime('12/Feb/2014:03:08:11 +0800')
def parselog(infile,outfile,dirtyfile):
    file=open(infile)
    output=open(outfile,'w')
    dirty=open(dirtyfile,'w')
    items=[
        r'(?P<ip>\S+)',
        r'\S+',
        r'(?P<user>\S+)',
        r'\[(?P<time>.*)\]',
        r'"(?P<request>.*)"',
        r'(?P<status>[0-9]+)',
        r'(?P<size>[0-9]+)',
        r'"(?P<referer>.*)"',
        r'"(?P<agent>.*)"',
        r'(.*)'
    ]
    pattern=re.compile(r'\s+'.join(items)+r'\s*\Z')#\s是指空白，包括空格、换行、tab缩进等所有的空白，而\S刚好相反
    #\Z从字符串结束处匹配。
    for line in file:
        m=pattern.match(line)
        #if not m:
            #dirty.write(line)
        #else:
        dict=m.groupdict()
        #dict['time']=converttime(dict['time'])
        print [dict['ip'],dict['user'],dict['time'],dict['request'],dict['status'],dict['size'],dict['referer'],dict['agent']]
        #print dict['referer']
print parselog('coolshell.txt','outfile.txt','dirty.txt')
