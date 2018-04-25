#_*_ coding:UTF-8 _*_
import json
import os
import sys

'''
#6XX shandong IPMI ping test
server_ip = {
    '10.0.0.1':'Server Name 1',
    '10.0.0.2':'Server Name 2'
}
'''

def createfile():
    if os.path.exists('PINGLOG.txt'):
        os.remove('PINGLOG.txt')
    if os.path.exists('PINGREPORT.txt'):
        os.remove('PINGREPORT.txt')

    file1 = open('PINGLOG.txt', 'w')
    file1.close()

    file2 = open('PINGREPORT.txt', 'w')
    file2.close()

    # The title infomation to write to file
    os.system('echo IPMI PING TEST >> PINGLOG.txt')
    os.system('echo --------------- >> PINGLOG.txt')

def pingresulte2file():
    oscmd = 'ping ' + str(key) + ' -c 4' + ' >> PINGLOG.txt'
    server_name = 'echo NAME:' + str(server_ip[key]) + ' >> PINGLOG.txt'
    os.system('date >> PINGLOG.txt')
    # os.system('time /t >> PINGLOG.txt')
    #print(oscmd)
    os.system(server_name)
    os.system(oscmd)
    os.system('echo --------------- >> PINGLOG.txt')

def checkservererr():
    s = os.popen('ping ' + str(key) + ' -c 4')
    err_server = s.readlines()
    #print(err_server)
    #print(err_server[3])
    kword = err_server[3]
    #print(kword[35:39])


    #err_server[3].find('100%') or err_server[3].find('75%') or err_server[3].find('50%') or err_server[3].find('25%')
    if  kword[35:39] == '100%' :
        err_server = 'echo ' + server_ip[key] + '/' + key + ': Failed >> PINGREPORT.txt'
        os.system(err_server)

def showinfo():
    global finish
    per = int(len(server_ip))
    #print(str(per) + ' ' + str(finish/per))
    sys.stdout.write('\r Finished : %s' % int(100*finish/per) + '%')
    sys.stdout.flush()
    finish = finish + 1


createfile()
finish = 1
f = open("serveripadd.json")
server_ip = json.load(f)
for key in server_ip.keys():
    pingresulte2file()
    checkservererr()
    showinfo()

print('\n')




