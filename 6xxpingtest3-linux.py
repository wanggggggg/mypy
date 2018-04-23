#_*_ coding:UTF-8 _*_
import os,sys,time,json
'''
#6XX shandong IPMI ping test
server_ip = {
    '10.85.34.1':'server one',
    '10.85.34.2':'server two',
    '192.168.0.254':'MY ROUTE'
}
'''

def createfile():
    if os.path.exists('6XXPING.txt'):
        os.remove('6XXPING.txt')
    if os.path.exists('6XXPINGREPORT.txt'):
        os.remove('6XXPINGREPORT.txt')

    file1 = open('6XXPING.txt', 'w')
    file1.close()

    file2 = open('6XXPINGREPORT.txt', 'w')
    file2.close()

    # The title infomation to write to file
    os.system('echo 6XX IPMI PING TEST >> 6XXPING.txt')
    os.system('echo --------------- >> 6XXPING.txt')

def pingresulte2file():
    oscmd = 'ping ' + str(key) + ' -c 4' + ' >> 6XXPING.txt'
    server_name = 'echo NAME:' + str(server_ip[key]) + ' >> 6XXPING.txt'
    os.system('date >> 6XXPING.txt')
    #os.system('time /t >> 6XXPING.txt')
    #print(oscmd)
    os.system(server_name)
    os.system(oscmd)
    os.system('echo --------------- >> 6XXPING.txt')

def checkservererr():
    s = os.popen('ping ' + str(key) + ' -c 4')
    err_server = s.readlines()
    #print(err_server)
    #print(err_server[3])
    kword = err_server[3]
    #print(kword[35:39])


    #err_server[3].find('100%') or err_server[3].find('75%') or err_server[3].find('50%') or err_server[3].find('25%')
    if  kword[35:39] == '100%' :
        err_server = 'echo ' + server_ip[key] + '/' + key + ': Failed >> 6XXPINGREPORT.txt'
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




