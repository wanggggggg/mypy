#_*_ coding:UTF-8 _*_
import json
import os
import sys

'''
#6XX shandong IPMI ping test
server_ip = {
    '10.85.34.1':'server one',
    '10.85.34.2':'server two',
    '192.168.0.254':'MY ROUTE'
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
    os.system('echo 6XX IPMI PING TEST >> PINGLOG.txt')
    os.system('echo --------------- >> PINGLOG.txt')

def pingresulte2file():
    oscmd = 'ping ' + str(key) + ' >> PINGLOG.txt'
    server_name = 'echo NAME:' + str(server_ip[key]) + ' >> PINGLOG.txt'
    os.system('date /t >> PINGLOG.txt')
    os.system('time /t >> PINGLOG.txt')
    os.system(server_name)
    os.system(oscmd)
    os.system('echo --------------- >> PINGLOG.txt')

def checkservererr():
    s = os.popen('ping ' + str(key))
    err_server = s.readlines()
    #print(err_server)

    for i in err_server:
        if i == 'Request timed out.\n':
            err_server = 'echo ' + server_ip[key] + '/ * /' + key + ': Failed >> PINGREPORT.txt'
            os.system(err_server)
            break
def showinfo():
    global finish
    per = int(len(server_ip))
    sys.stdout.write('\r Finished : %s' % int(100*finish/per) + '%')
    sys.stdout.flush()
    finish = finish + 1


createfile()
f = open("serveripmi.json", encoding='utf-8')
server_ip = json.load(f)
finish = 1

for key in server_ip.keys():
    pingresulte2file()
    checkservererr()
    showinfo()
print('\n')





