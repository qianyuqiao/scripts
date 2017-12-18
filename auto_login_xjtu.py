import requests
import sys

def login(type):
    headers =  {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Encoding': 'gzip, deflate, sdch, br',
         'Accept-Language': 'zh-CN,zh;q=0.8',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    s = requests.Session()
    s.headers = headers
    post_data = {'username': 'qianyuqiao', 'password': '464302'}
    r = s.post('http://10.6.8.2:901/srun_portal_pc.php?ac_id=1&', data=post_data, verify=False)
    print "log in, status = %s" % r.status_code
 
''' 
def logout(type):
    """logout work"""
    headers =  {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Encoding': 'gzip, deflate, sdch, br',
         'Accept-Language': 'zh-CN,zh;q=0.8',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    s = requests.Session()
    s.headers = headers
    post_data = {'username': 'username', 'password': 'password', 'iprange': 'no'}
    s.post('https://its.pku.edu.cn/cas/webLogin', data=post_data, verify=False)
    #to logout!!
    r = s.get('https://its.pku.edu.cn/netportal/ITSipgw?cmd=close&type=%s&sid=478' % type, verify=False, headers=headers)
    print "log out, status = %s" % r.status_code
 
 '''
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "usage <option: 1 (connect free), 2 (connect global), 3 (disconnect this computer), 4 (disconnect all), 5(disconnect this computer and connect free)"
        exit(1)
        
    option = int(sys.argv[1])
    if option == 1:
        print "try to connect free"
        login('no')
    elif option == 2:
        print "try to connect global"
        login('yes')
    elif option == 3:
        print "try to disconnect self"
        logout('self')
    elif option == 4:
        print "try to disconnect all"
        logout('all')