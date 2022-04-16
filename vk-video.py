import vk_api            #API vk.com
from os import system    #команды для консоли

system("termux-wake-lock")

#ЗАСТАВКА
def banner():
    system("clear")
    print("\033[34m        _             \033[35m         _      _              ")
    print("\033[34m       | | __         \033[35m        (_)    | |             ")
    print("\033[34m  __   |__/ /         \033[35m__    __ _  ___| | ____  ____  ")
    print("\033[34m  \ \  / / /   _____  \033[35m\ \  / /| |/ __  |/ __ \/    \ ")
    print("\033[34m   \ \/ /  \  |\033[35m_____|  \ \/ / | | (__| |  ___/  () | ")
    print("\033[34m    \__/_|\_\         \033[35m  \__/  |_|\___._|\____|\____/ ")
    print("\033[0m")
banner()
print("\033[0m кинь хотя бы 1₽ \033[33mhttps://qiwi.com/n/AMODE174 \033[0m:3\n")


token = open('token.txt')
token = token.readline()
token = token[:-1]
text = open('text.txt')
text = text.readlines()
del text[0:20]
print("\033[33m            команды\033[0m\n")
for i in text:
    i = i[:-1]
    print(f" {i}")

print(f"\n для выхода \033[33mCTRL\033[0m + \033[33mZ\033[0m\n")

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api() #авторизация
pidaras = vk.account.getProfileInfo()['id'] #id юзера


ts = vk.messages.getLongPollServer()['ts'] #номер последнего события
pts = vk.messages.getLongPollHistory(ts= ts)['new_pts'] #аналог ts

while True:
    pts = vk.messages.getLongPollHistory(pts= pts)['new_pts']
    zaebal = vk.messages.getLongPollHistory(pts= pts)

    while zaebal['new_pts'] == zaebal['from_pts']:
        zaebal = vk.messages.getLongPollHistory(pts= pts)
    
    penis = zaebal['messages']['items'][0]
    if penis['from_id'] == pidaras:
        for i in text:
            i = i[:-1]
            i1 = i.partition('||')[0]
            i2 = i.partition('||')[2]
            if penis['text'] == i1:
                vk.messages.edit(peer_id= penis['peer_id'], message_id= penis['id'], attachment=i2, keep_forward_messages = 1)






    