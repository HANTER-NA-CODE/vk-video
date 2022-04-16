import vk_api            #API vk.com
from time import sleep   #таймер
from os import system    #команды для консоли

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
print("  код запущен")
print(f"\n для выхода \033[33mCTRL\033[0m + \033[33mZ\033[0m\n")

#ПЕРЕМЕННЫЕ
token = open('token.txt') #открывает файл с токеном
token = token.readline() #принимает значение файла
token = token[:-1] #обрезает последний символ строки, це перенос

#АВТОРИЗАЦИЯ
session = vk_api.VkApi(token=token)
vk = session.get_api()

#ОСНОВНОЙ КОД
pidaras = vk.account.getProfileInfo()['id'] #id пользователя
penis = 0 #id последнего смс

while True:
    ts = vk.messages.getLongPollServer()['ts'] #id последнего действия
    her = vk.messages.getLongPollHistory(ts=ts)
    
    while her['messages']['count'] == 0:
        her = vk.messages.getLongPollHistory(ts=ts)
        sleep(0.1)

    zalupa = her['messages']['items'][-1]

    if penis != zalupa['id']:
        penis = zalupa['id']
        if zalupa['from_id'] == pidaras:
            if zalupa['text'] == '/yes':
                vk.messages.edit(peer_id= zalupa['peer_id'], message_id= zalupa['id'], attachment="video379692532_456239486", keep_forward_messages= 1)
            elif zalupa['text'] == '/no':
                vk.messages.edit(peer_id= zalupa['peer_id'], message_id= zalupa['id'], attachment="video493443736_456240604", keep_forward_messages= 1)
            elif zalupa['text'] == '/ahah':
                vk.messages.edit(peer_id= zalupa['peer_id'], message_id= zalupa['id'], attachment="video493443736_456240606", keep_forward_messages= 1)
            elif zalupa['text'] == '/be':
                vk.messages.edit(peer_id= zalupa['peer_id'], message_id= zalupa['id'], attachment="video493443736_456240605", keep_forward_messages= 1)
            elif zalupa['text'] == '/пока':
                vk.messages.edit(peer_id= zalupa['peer_id'], message_id= zalupa['id'], attachment="video50476600_456239285", keep_forward_messages= 1)
            elif zalupa['text'] == '/разрывная':
                vk.messages.edit(peer_id= zalupa['peer_id'], message_id= zalupa['id'], attachment="video-200042852_456239190", keep_forward_messages= 1)
            elif zalupa['text'] == '/наебали':
                vk.messages.edit(peer_id= zalupa['peer_id'], message_id= zalupa['id'], attachment="video285684542_456239033", keep_forward_messages= 1)
            elif zalupa['text'] == '/да ну нахуй':
                vk.messages.edit(peer_id= zalupa['peer_id'], message_id= zalupa['id'], attachment="video280391488_456239116", keep_forward_messages= 1)
            elif zalupa['text'] == '/похлопаю':
                vk.messages.edit(peer_id= zalupa['peer_id'], message_id= zalupa['id'], attachment="video-51171511_170851952", keep_forward_messages= 1)
    
            





    