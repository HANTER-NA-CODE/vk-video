'''*******************************************************   БИБЛИОТЕКИ  **************************************************************'''

import sqlite3
from requests import post
from requests import get as down
from os import system as terminal
from time import sleep
import vk





'''*****************************************************   БАЗА ДАННЫХ   **************************************************************'''

conn = sqlite3.connect('vk-video.db') #база данных
cur = conn.cursor() #курсор бд

cur.execute("""CREATE TABLE IF NOT EXISTS user(token TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS shab(message TEXT, attachment TEXT)""")





'''**********************************************************   БАННЕР   **************************************************************'''

def banner():
    terminal("clear")
    print("\033[34m        _             \033[35m         _      _              "); sleep(0.02)
    print("\033[34m       | | __         \033[35m        (_)    | |             "); sleep(0.02)
    print("\033[34m  __   |__/ /         \033[35m__    __ _  ___| | ____  ____  "); sleep(0.02)
    print("\033[34m  \ \  / / /   _____  \033[35m\ \  / /| |/ __  |/ __ \/    \ "); sleep(0.02)
    print("\033[34m   \ \/ /  \  |\033[35m_____|  \ \/ / | | (__| |  ___/  () | "); sleep(0.02)
    print("\033[34m    \__/_|\_\         \033[35m  \__/  |_|\___._|\____|\____/ "); sleep(0.02)
    print("\033[0m                                            HANTER-NA-CODE\n"); sleep(0.02)






'''**********************************************************   ШАБЛОНЫ   **************************************************************'''

def get():
    cur.execute(f"SELECT rowid, * FROM shab")
    shab = cur.fetchall()
    print('\033[91m  айди                \033[92m вложение                         \033[0m сообщение\n')
    for i in shab:
        print('\033[91m' + '   ' + str(i[0]) + ' '*(4-len(str(i[0]))) + '\033[35m' + ' ---   ' + '\033[92m' + str(i[2]) + ' '*(30-len(str(i[2]))) + '\033[35m' + '   ---   ' + '\033[0m' + str(i[1]))
        sleep(0.02)
    print(); sleep(0.02)
    print(" \033[91m[\033[0m1\033[91m]\033[93m добавить"); sleep(0.02)
    print(" \033[91m[\033[0m2\033[91m]\033[93m изменить"); sleep(0.02)
    print(" \033[91m[\033[0m3\033[91m]\033[93m удалить"); sleep(0.02)
    print(" \033[91m[\033[0m4\033[91m]\033[93m удалить все"); sleep(0.02)
    print(" \033[91m[\033[0m0\033[91m]\033[93m выйти"); sleep(0.02)
    print("\033[0m"); sleep(0.02)
    def vibr():
        pok = input("\033[92m выбери вариант: \033[96m"); print("\033[0m")
        if pok == '1':
            print("\033[0m")
            attachment = input("\033[92m вложение: \033[96m")
            message = input("\033[92m сообщение: \033[96m"); print("\033[0m")

            cur.execute(f"INSERT INTO shab VALUES('{message}', '{attachment}')")
            conn.commit()
            banner()
            get()
        elif pok == '2':
            id = input("\n\033[92m айди шаблона: \033[96m"); print("\033[0m")
            attachment = input("\033[92m новое вложение: \033[96m"); 
            message = input("\033[92m новое сообщение: \033[96m"); print("\033[0m")
            try:
                cur.execute(f"""UPDATE shab SET message = '{message}', attachment = '{attachment}' WHERE rowid = {id}""")
                conn.commit()
            except:
                print('\033[91m ОШИБКА\033[0m скорее всего вы что то неправильно ввели')
                sleep(3)
            banner()
            get()
        elif pok == '3':
            id = input("\n\033[92m айди шаблона: \033[96m"); print("\033[0m")
            cur.execute(f"""DELETE from shab WHERE rowid = {id}""")
            conn.commit()
            banner()
            get()
        elif pok == '4':
            cur.execute(f"""DELETE from shab""")
            conn.commit()
            banner()
            get()
        elif pok == '0':
            banner()
            menu()
        else:
            print('\033[91m ОШИБКА\033[0m скорее всего вы что то неправильно ввели\n')
            vibr()
    vibr()






'''******************************************************   СМЕНИТЬ ТОКЕН   **************************************************************'''

def sm_token():
    print("\033[93m  получить \033[91maccess token"); sleep(0.02)
    print("\033[93m  можно по ссылке \033[91mhttps://vkhost.github.io\n")
    print("\033[91m  [\033[0m0\033[91m]\033[93m для отмены\n\n"); sleep(0.02)
    pok = input("\033[92m token: \033[96m"); print("\033[0m")
    if pok == '0':
        pass
    else:
        cur.execute(f"INSERT INTO user VALUES('{pok}')")
        #cur.execute(f"UPDATE user SET token = '{pok}' WHERE rowid = 1")
        conn.commit()
    banner()
    menu()





'''**********************************************************   ПАРСЕР   **************************************************************'''

def pars():
    banner()
    cur.execute(f"SELECT token FROM user")
    li = cur.fetchall()
    vk.auth(token = li[-1][0], vers = 5)

    cur.execute(f"""DELETE from shab""")
    try:
        posts = vk.method('wall.get',
          "owner_id=-212708924&"
        + "count=100&"
        + "offset=0" )
    except:
        print('\033[91m ОШИБКА\033[0m скорее всего неправильный токен или нет интернета\n')
        sleep(2)
        banner()
        menu()
    
    cur.execute(f"""DELETE from shab""")

    x = 1
    while len(posts['items']) != 0:
        for post in posts['items']:
            if 'is_pinned' in post.keys():
                continue
                
            toto = post['attachments'][0]
            oko = toto['type']
            message = post['text']
            attachment = f"{oko}{toto[oko]['owner_id']}_{toto[oko]['id']}"
            
            cur.execute(f"INSERT INTO shab VALUES('{message}', '{attachment}')")

            print('  \033[92m' + attachment + ' '*(30-len(attachment)) + '\033[35m   ---   \033[0m' + message)
            x += 1
            sleep(0.02)

        posts = vk.method('wall.get',
          "owner_id=-212708924&"
        + "count=100&"
        + f"offset={x}" )

    conn.commit()
    sleep(1)
    banner()
    menu()





'''*********************************************************   СКАЧАТЬ ШАБЛОН   ********************************************************'''

def skach():
    try:
        banner()
        print(' шаблоны публикуются тут > \033[91mhttps://vk.com/topic-212708924_48629464\033[0m <\n')
        cur.execute(f"SELECT token FROM user")
        li = cur.fetchall()
        vk.auth(token = li[-1][0], vers = 5.131)
        try:
            vk.method('account.getProfileInfo')   #проверка токена
        except:
            print('\033[91m ОШИБКА\033[0m скорее всего неправильный токен или нет интернета\n')
            sleep(2)
            banner()
            menu()

        global name
        name = input("\033[92m имя шаблона: \033[96m")
        print()
        if name == '0':
            banner()
            menu()
        for i in vk.method('board.getComments', f'group_id=212708924&' + f'topic_id=48629464&')['items']:
            if name == i['text']:
                url = i['attachments'][0]['doc']['url'] 


        shabs = open('shab.txt', 'wb')

        file = down(url)
        shabs.write(file.content)
        shabs.close()


        cur.execute(f"""DELETE from shab""")


        shabs = open('shab.txt', 'r', encoding='utf-8')
        for shab in shabs.readlines():
            shab = shab[:-1].partition(' || ')
            cur.execute(f"INSERT INTO shab VALUES('{shab[2]}', '{shab[0]}')")
            print('  \033[92m' + shab[0] + ' '*(30-len(shab[0])) + '\033[35m   ---   \033[0m' + shab[2]); sleep(0.02)

        sleep(1)
        conn.commit()
        shabs.close()  
        banner()
        menu()
    except:
        print('\033[91m ОШИБКА\033[0m скорее всего вы что то неправильно ввели\n')
        sleep(3)
        banner()
        menu()






'''*******************************************************   ВЫГРУЗИТЬ ШАБЛОН   ********************************************************'''

def vigr():
    banner()
    print(' шаблоны публикуются тут > \033[91mhttps://vk.com/topic-212708924_48629464\033[0m <\n')
    cur.execute(f"SELECT token FROM user")
    li = cur.fetchall()
    vk.auth(token = li[-1][0], vers = 5.131)
    try:
        vk.method('account.getProfileInfo')   #проверка токена
    except:
        print('\033[91m ОШИБКА\033[0m скорее всего неправильный токен или нет интернета\n')
        sleep(2)
        banner()
        menu()
    
    #**********   СОЗДАНИЕ ФАЙЛА shab.txt   ***************
    shabs = open('shab.txt', 'w', encoding='utf-8')
    cur.execute(f"SELECT * FROM shab")
    for shab in cur.fetchall():
        shabs.write(shab[1] + ' || ' + shab[0] + '\n')
    shabs.close()



    def name_shab():
        global name
        name = input("\033[92m создайте имя шаблону: \033[96m")

        if name == '0':
            banner()
            menu()

        for i in vk.method('board.getComments', f'group_id=212708924&' + f'topic_id=48629464&')['items']:
            if name == i['text']:
                print('\n\033[91m ОШИБКА\033[0m такое имя уже есть, попробуй другое\n')
                name_shab()
        
    name_shab()

    url = vk.method('docs.getUploadServer')['upload_url']          #ссылка для загрузки файла
    response = post(url, files={'file': open('shab.txt', 'rb')})   #загрузка файла
    file = response.json()['file']                                 #ответ сервера
    file = vk.method('docs.save', f'file={file}')['doc']           #сохранение файла
    
    file = f"doc{file['owner_id']}_{file['id']}"
    vk.method('board.createComment', f'group_id=212708924&' + f'topic_id=48629464&' + f'message={name}&' + f'attachment={file}&' + f'guid=0')

    print(f'\n\033[0m теперь твой\033[91m шаблон\033[0m можно скачать в пункте \033[91m5\033[0m под именем \033[91m{name}\033[0m\n')

    input("\033[92m напишите что-нибудь, чтобы вернуться в меню: \033[96m")
    banner()
    menu()





'''*******************************************************   ЗАПУСТИТЬ   **************************************************************'''

def main():
    try:
        try:
            cur.execute(f"SELECT token FROM user")
            li = cur.fetchall()
            vk.auth(token = li[-1][0], vers = 5.131)
            user = vk.method('account.getProfileInfo')['id']
        except:
            print('\033[91m ОШИБКА\033[0m скорее всего неправильный токен или нет интернета\n')
            sleep(2)
            banner()
            menu()

        cur.execute(f"SELECT rowid, * FROM shab")
        shab = cur.fetchall()
        print('          \033[92m вложение                        \033[0m сообщение\n')
        for i in shab:
            print('    ' + '\033[92m' + str(i[2]) + ' '*(30-len(str(i[2]))) + '\033[35m' + '   ---   ' + '\033[0m' + str(i[1]))
            sleep(0.02)

        print(f"\n для выхода \033[91mCTRL\033[0m + \033[91mC\033[0m\n")


        ts = vk.method('messages.getLongPollServer')['ts']
        pts = vk.method('messages.getLongPollHistory', f'ts={ts}')['new_pts'] 
    
    
        while True:
            pts = vk.method('messages.getLongPollHistory', f'ts={ts}')['new_pts']
            sobitie = vk.method('messages.getLongPollHistory', f'pts={pts}')

            while sobitie['new_pts'] == sobitie['from_pts']:
                sobitie = vk.method('messages.getLongPollHistory', f'pts={pts}')

            if len(sobitie['messages']['items']) != 0:
                message = sobitie['messages']['items'][0]
                if message['from_id'] == user:
                    for i in shab:
                        if message['text'].lower() == i[1]:
                            vk.method('messages.edit',
                              f'peer_id={message["peer_id"]}&'
                            + f'message_id={message["id"]}&'
                            + f'attachment={i[2]}&'
                            + f'keep_forward_messages=1&' )
    except:   
        banner()
        menu()






'''***********************************************************   МЕНЮ   *****************************************************************'''

def menu():
    print(); sleep(0.02)
    print(" \033[91m[\033[0m1\033[91m]\033[93m запустить"); sleep(0.02)
    print(" \033[91m[\033[0m2\033[91m]\033[93m сменить токен"); sleep(0.02)
    print(" \033[91m[\033[0m3\033[91m]\033[93m шаблоны"); sleep(0.02)
    print(" \033[91m[\033[0m4\033[91m]\033[93m скачать основной шаблон"); sleep(0.02)
    print(" \033[91m[\033[0m5\033[91m]\033[93m скачать шаблон на выбор"); sleep(0.02)
    print(" \033[91m[\033[0m6\033[91m]\033[93m поделиться своим шаблоном"); sleep(0.02)
    print(" \033[91m[\033[0m0\033[91m]\033[93m закрыть"); sleep(0.02)
    print("\033[0m"); sleep(0.02)
    def vibr():
        pok = input("\033[92m выбери вариант: \033[96m"); print("\033[0m")
        if pok == '1':
            banner()
            main()
        elif pok == '2':
            banner()
            sm_token()
        elif pok == '3':
            banner()
            get()
        elif pok == '4':
            pars()
        elif pok == '5':
            skach()
        elif pok == '6':
            vigr()
        elif pok == '0':
            exit()
        else:
            print('\033[91m ОШИБКА\033[0m скорее всего вы что то неправильно ввели\n')
            vibr()
    vibr()






'''******************************************************   ВЫЗОВ МЕНЮ   ***************************************************************'''

banner()
menu()