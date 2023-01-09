'''
=============SON OF GENISYS=====================
Astra members adding script
Coded by a dumbass kid- github.com/Cryptonian007
Apologies if anything in the code is dumb :)
Copy with credits
************************************************
'''

# import libraries
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel, ChannelParticipantsSearch
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest, GetParticipantsRequest
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
import time
import random
from colorama import init, Fore
import os
import pickle


init()


r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs

def banner():
    # fancy logo
    b = [
'--------------------------',    
'USER ADDER V1.0',
'--------------------------',
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{rs}')
    #print('=============SON OF GENISYS==============')
    print(f'{lg}   Versiyon: {w}1.2{lg} | Geliştirici: {w}PikaTube{rs}\n')


# function to clear screen
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

# create sessions(if any) and check for any banned accounts
# TODO: Remove code input(just to check if an account is banned)
print('\n' + info + lg + ' Spamlı Hesaplar Taranıyor...' + rs)
for a in accounts:
    phn = a[0]
    print(f'{plus}{grey} Temiz {lg}{phn}')
    clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            print('OK')
        except PhoneNumberBannedError:
            print(f'{error} {w}{phn} {r}Spamlı{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print(info+lg+' Yasaklı Hesaplar Kaldırıldı[Remove permanently using manager.py]'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' Hesaplar Oluşturuldu')
clr()
banner()
# func to log scraping details(link of the grp to scrape
# and current index) in order to resume later
def log_status(scraped, index):
    with open('status.dat', 'wb') as f:
        pickle.dump([scraped, int(index)], f)
        f.close()
    print(f'{info}{lg} Hesap kaydedildi {w}status.dat{lg}')
    

def exit_window():
    input(f'\n{cy} Çıkış için entere basın...')
    clr()
    banner()
    sys.exit()

# read user details
try:
    # rquest to resume adding
    with open('status.dat', 'rb') as f:
        status = pickle.load(f)
        f.close()
        lol = input(f'{INPUT}{cy} son gruptan işleme devam edilsin mi {w}{status[0]}{lg}? [y/n]: {r}')
        if 'y' in lol:
            scraped_grp = status[0] ; index = int(status[1])
        else:
            if os.name == 'nt': 
                os.system('del status.dat')
            else: 
                os.system('rm status.dat')
            scraped_grp = input(f'{INPUT}{cy} Herkese Acık bir grup linki belirtiniz: {r}')
            index = 0
except:
    scraped_grp = input(f'{INPUT}{cy} Herkese açık bir grup linki belirtiniz: {r}')
    index = 0
# load all the accounts(phonenumbers)
accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

print(f'{info}{lg} Tüm Hesaplar: {w}{len(accounts)}')
number_of_accs = int(input(f'{INPUT}{cy} Kullanılacak Hesap Sayısı: {r}'))
print(f'{info}{cy} Bir Seçenek belirtiniz {lg}')
print(f'{cy}[0]{lg} Herkese açık grup')
print(f'{cy}[1]{lg} Gizli grup ')
choice = int(input(f'{INPUT}{cy} Seçım belirtiniz: {r}'))
if choice == 0:
    target = str(input(f'{INPUT}{cy} Hangi gruba üye Çekilecek: {r}'))
else:
    target = str(input(f'{INPUT}{cy} Gizli olan grup : {r}'))
print(f'{grey}_'*50)
#status_choice = str(input(f'{INPUT}{cy} Do you wanna add active members?[y/n]: {r}'))
to_use = [x for x in accounts[:number_of_accs]]
for l in to_use: accounts.remove(l)
with open('vars.txt', 'wb') as f:
    for a in accounts:
        pickle.dump(a, f)
    for ab in to_use:
        pickle.dump(ab, f)
    f.close()
sleep_time = int(input(f'{INPUT}{cy} Geçikme süresi belirtin{w}[{lg} 0 ve 59 saniye arasında{w}]: {r}'))
#print(f'{info}{lg} Joining group from {w}{number_of_accs} accounts...')
#print(f'{grey}-'*50)
print(f'{success}{lg} -- üye ekleme {w}{len(to_use)}{lg} Hesap(s) --')
adding_status = 0
approx_members_count = 0
for acc in to_use:
    stop = index + 60
    c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
    print(f'{plus}{grey} Kullanıcı: {cy}{acc[0]}{lg} -- {cy}Başlangıç oturumu... ')
    c.start(acc[0])
    acc_name = c.get_me().first_name
    try:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            try:
                c(ImportChatInviteRequest(g_hash))
                print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- İşlem için Gruba katıldı')
            except UserAlreadyParticipantError:
                pass 
        else:
            c(JoinChannelRequest(scraped_grp))
            print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- İşlem için Gruba katıldı')
        scraped_grp_entity = c.get_entity(scraped_grp)
        if choice == 0:
            c(JoinChannelRequest(target))
            print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- Üye ekleme için katıldı')
            target_entity = c.get_entity(target)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        else:
            try:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- Üye ekleme için katıldı')
            except UserAlreadyParticipantError:
                pass
            target_entity = c.get_entity(target)
            target_details = target_entity
    except Exception as e:
        print(f'{error}{r} Kullanıcı: {cy}{acc_name}{lg} -- Gruba Katılamadı')
        print(f'{error} {r}{e}')
        continue
    print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {cy}Kullanıcıları alma...')
    #c.get_dialogs()
    try:
        members = []
        while_condition = True
        my_filter = ChannelParticipantsSearch('')
        offset = 0
        i = 1
        while while_condition:
            participants = c(GetParticipantsRequest(channel=scraped_grp,  offset= offset, filter = my_filter, limit=200, hash=0))
            members.extend(participants.users)
            offset += len(participants.users)
            members += (participants.users)
            if len(participants.users) < 1 :
                while_condition = False
    except Exception as e:
        print(f'{error}{r} Couldn\'üyeler çekiliyor')
        print(f'{error}{r} {e}')
        continue
    approx_members_count = len(members)
    assert approx_members_count != 0
    if index >= approx_members_count:
        print(f'{error}{lg} Eklenecek üye yok!')
        continue
    print(f'{info}{lg} Başlangıç: {w}{index}')
    #adding_status = 0
    peer_flood_status = 0
    for user in members[index:stop]:
        index += 1
        if peer_flood_status == 10:
            print(f'{error}{r} Çok fazla Deneme...')
            break
        try:
            if choice == 0:
                c(InviteToChannelRequest(target_details, [user]))
            else:
                c(AddChatUserRequest(target_details.id, user, 42))
            user_id = user.first_name
            target_title = target_entity.title
            print(f'{plus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {cy}{user_id} {lg}--> {cy}{target_title}')
            #print(f'{info}{grey} Kullanıcı: {cy}{acc_name}{lg} -- 1 saniye bekle')
            adding_status += 1
            print(f'{info}{grey} Kullanıcı: {cy}{acc_name}{lg} -- bekle {w}{sleep_time} {lg}Bekleme(s)')
            time.sleep(sleep_time)
        except UserPrivacyRestrictedError:
            print(f'{minus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r}Kullanıcı Gizliliği Sınırlı Hata')
            continue
        except PeerFloodError:
            print(f'{error}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r}Hata.')
            peer_flood_status += 1
            continue
        except ChatWriteForbiddenError:
            print(f'{error}{r} Can\' Gruba eklenemiyor grup izinlerini degiştiriniz')
            if index < approx_members_count:
                log_status(scraped_grp, index)
            exit_window()
        except UserBannedInChannelError:
            print(f'{error}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r} Yasaklandım :( Mesaj yazamıyorum')
            break
        except ChatAdminRequiredError:
            print(f'{error}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r}Grup Yöneticisi için gerekli haklar')
            continue
        except UserAlreadyParticipantError:
            print(f'{minus}{grey} Kullanıcı: {cy}{acc_name}{lg} -- {r} Bu Kullanıcı Zaten Grupta var!')
            continue
        except FloodWaitError as e:
            print(f'{error}{r} {e}')
            break
        except ValueError:
            print(f'{error}{r} kullanıcı Hatası')
            continue
        except KeyboardInterrupt:
            print(f'{error}{r} ---- Ekleme işlemi durduruldu ----')
            if index < len(members):
                log_status(scraped_grp, index)
            exit_window()
        except Exception as e:
            print(f'{error} {e}')
            continue
#global adding_status, approx_members_count
if adding_status != 0:
    print(f"\n{info}{lg} Hesap ekleme sona erdi")
try:
    if index < approx_members_count:
        log_status(scraped_grp, index)
        exit_window()
except:
    exit_window()
