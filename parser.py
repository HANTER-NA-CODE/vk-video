from time import sleep
import vk_api            #API vk.com
from os import system

#ЗАСТАВКА
def banner():
    #system("cls") #вводит "clear" в терминал, це очищает консоль
    print("\033[34m        _             \033[35m         _      _              ")
    print("\033[34m       | | __         \033[35m        (_)    | |             ")
    print("\033[34m  __   |__/ /         \033[35m__    __ _  ___| | ____  ____  ")
    print("\033[34m  \ \  / / /   _____  \033[35m\ \  / /| |/ __  |/ __ \/    \ ")
    print("\033[34m   \ \/ /  \  |\033[35m_____|  \ \/ / | | (__| |  ___/  () | ")
    print("\033[34m    \__/_|\_\         \033[35m  \__/  |_|\___._|\____|\____/ ")
    print("\033[0m")
banner()

#ПЕРЕМЕННЫЕ
text = open("text.txt", 'w')
texts = ['чтобы начать редактировать\n', 'нажми "a" на английской клавиатуре\n', '\n', 'добавляй команды по шаблону ниже\n', 'команда||id вложения\n', '\n', 'ограничений на количество команд нет, добовляй сколько хочешь\n', '\n', 'чтобы сохранить и выйти:\n', 'нажми "ESC", затем напиши ":wq"\n', '\n', 'чтобы выйти без сохранения:\n', 'нажми "ESC", затем напиши ":q!"\n', '\n', '\n', '!!!РЕДАКТИРОВАТЬ МОЖНО ТОЛЬКО КОМАНДЫ!!!\n', '\n', '\n', ' КОМАНДЫ\n', '\n']

token = open('token.txt')
token = token.readline()
token = token[:-1]


vk_session = vk_api.VkApi(token = token)
vk = vk_session.get_api()
grup = -212708924

#ПАРСЕР
print("\n            ПАРСЕР\n")

posts = vk.wall.get(owner_id = grup, count = 100, offset= 0)
x = 1
while len(posts['items']) != 0:
    for i in posts['items']:
        if 'is_pinned' in i.keys():
            continue
        
        toto = i['attachments'][0]
        oko = toto['type']
        
        shab = f"{i['text']}||{oko}{toto[oko]['owner_id']}_{toto[oko]['id']}\n"
        print(f"{x}) {shab[0:-1]}")
        texts.append(shab)
        x += 1
        sleep(0.02)
    posts = vk.wall.get(owner_id = grup, count = 100, offset= x)

#ДОБАВЛЕНИЕ КОММАНД В ФАЙЛ    
for i in texts:
    text.write(i)
    