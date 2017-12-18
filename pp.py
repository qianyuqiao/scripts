import pcap
import dpkt
from cheat_ip import Iplist
import socket

ssh_status=['']

def handle(sig):
    if sig == 0:
        return True
    if sig == 22 :
        docker_cheat()
        port_redirect()


def ssh_check(data):
    if data.status='New Key':
        ssh_status.popall()
        ssh_status.append('New Key')

        


class  attack_check():
    def __init__(self,proto,data):
        if proto='SSH'
            self.attack=ssh_check(data)
            if self.attack != 0:
                return self.attack
            else:
                return 0

def captData():
    pc=pcap.pcap('eth0')
    global f
    f=open('/home/qianyuqiao/1.txt','w')
    for ptime,pdata in pc:    
        sig=anlyCap(pdata)
        if sig != 0:
            handle(sig)

    f.close() 

def anlyCap(pdata):
    p=dpkt.ethernet.Ethernet(pdata)
    if p.data.__class__.__name__=='IP':
        ip=p.data
        src = socket.inet_ntoa(ip.src)
        dst = socket.inet_ntoa(ip.dst)
        proto=protocol(p)
        ty=proto(ty)
        attack= attack_check(proto)
        f.writelines('source ip:'+str(src)+'  destination ip:'+str(dst)+'\n')
        print 'src=',str(src),'  dst=',str(dst)
        return attack

captData();
