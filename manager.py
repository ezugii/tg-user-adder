from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Modül yükleniyor - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
'--------------------------',    
'USER ADDER V1.0',
'--------------------------',

    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF GENISYS==============')
    print(f'   Versiyon: 1.3 | Geliştirici: @PikaTube{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Yeni Hesap Ekleyin'+n)
    print(lg+'[2] Spamlı hesaplara bakın'+n)
    print(lg+'[3] Seçilen Hesapları Görüntüleyin'+n)
    print(lg+'[4] Güncelleme'+n)
    print(lg+'[5] Çıkış'+n)
    a = int(input('\nBir Seçim yapınız: '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Kaç Hesap Eklenecek: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Telefon numarası giriniz: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] numara vars.txt kaydedildi')
            clr()
            print(f'\n{lg} [*] Yeni kullanıcı oturum actı\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Giriş Başarılı')
                c.disconnect()
            input(f'\n Ana Menü İçin Entere Basın...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Hesap Yoktur Hesap Ekleyin Ve Tekrar Deneyin')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Kodu giriniz: '))
                        print(f'{lg}[+] {phone} Temiz Hesap{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' Spamlı Hesap!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Spamlı Hesap Bulunamadı')
                input('\nAna Menü için Entere Basın...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] Tüm Spamlı Hesaplar Kaldırıldı'+n)
                input('\nAna Menü için Entere Basın...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Silinecek Hesap Seçiniz\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Bir Seçim giriniz: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Hesap silindi{n}')
        input(f'\nAna Menü için Entere Basın...')
        f.close()
    elif a == 4:
        # thanks to github.com/th3unkn0n for the snippet below
        print(f'\n{lg}[i] Güncelleme Kontrol Ediliyor...')
        try:
            # https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt')
        except:
            print(f'{r} Bağlanın ve tekrar deneyin')
            print(f'{r} İnternete Baglanın ve Tekrar Deneyin')
            exit()
        if float(version.text) > 1.1:
            prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Güncelleme indiriliyor...')
                if os.name == 'nt':
                    os.system('del add.py')
                    os.system('del manager.py')
                else:
                    os.system('rm add.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/add.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/manager.py')
                print(f'{lg}[*] Versiyon Güncellendi: {version.text}')
                input('Çıkmak için entere basın...')
                exit()
            else:
                print(f'{lg}[!] Güncelleme iptal edildi.')
                input('Ana Menü için entere Basın...')
        else:
            print(f'{lg}[i] zaten güncel...')
            input('Ana Menü için entere Basın...')
    elif a == 5:
        clr()
        banner()
        exit()
