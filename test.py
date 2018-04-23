'''
#this is use to ping server and record time
import os
import sys
import time

i = 1
while i < 100:
    os.system('date /t >> pingtest.txt'),
    os.system('time /t >> pingtest.txt'),
    os.system('ping 172.16.10.228 >> pingtest.txt'),
    i = i + 1
    print('run :' + str(i) + ' times.'),
    time.sleep(60)



----------
version 2:
----------

'''

#this is use to ping server and record time
import os
import sys
import time

i = 1
while i < 100:
    os.system('date /t >> pingtest.txt'),
    os.system('time /t >> pingtest.txt'),
    os.system('ping 172.16.10.228 >> pingtest.txt'),
    os.system('echo ------------------------ >> pingtest.txt'),
    i = i + 1
    print('run :' + str(i) + ' times.'),
    time.sleep(60)