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
    oscmd = 'ping ' + str(key) + ' >> 6XXPING.txt'
    server_name = 'echo NAME:' + str(server_ip[key]) + ' >> 6XXPING.txt'
    os.system('date /t >> 6XXPING.txt')
    os.system('time /t >> 6XXPING.txt')
    os.system(server_name)
    
    os.system(oscmd)

    os.system('echo --------------- >> 6XXPING.txt')

def checkservererr():
    s = os.popen('ping ' + str(key))
    err_server = s.readlines()
    #print(err_server)

    for i in err_server:
        if i == 'Request timed out.\n':
            err_server = 'echo ' + server_ip[key] + '/ * /' + key + ': Failed >> 6XXPINGREPORT.txt'
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





