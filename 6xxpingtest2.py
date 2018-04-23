#_*_ coding:UTF-8 _*_
import os,sys,time

server_ip = {
    '10.85.34.1':'server one',
    '10.85.34.2':'server two',
    '192.168.0.254':'MY ROUTE'
}

os.system('echo 6XX PING TEST >> 6XXPING.txt')
os.system('echo --------------- >> 6XXPING.txt')

for key in server_ip.keys():

    oscmd = 'ping ' + str(key) + ' >> 6XXPING.txt'
    server_name = 'echo NAME:' + str(server_ip[key]) + ' >> 6XXPING.txt'
    os.system('date /t >> 6XXPING.txt')
    os.system('time /t >> 6XXPING.txt')
    os.system(server_name)
    os.system(oscmd)
    os.system('echo --------------- >> 6XXPING.txt')


    s = os.popen('ping ' + str(key))
    err_server = s.readlines()
    print(err_server)

    for i in err_server :
        if i == 'Request timed out.\n':
            err_server = 'echo ' + server_name + key + ': Failed >> 6XXPINGREPORT.txt'
            os.system(err_server)
            break




            '''
            err_server = 'echo ' + server_name + key + ': Okay >> 6XXPINGREPORT.txt'
            os.system(err_server)
'''



