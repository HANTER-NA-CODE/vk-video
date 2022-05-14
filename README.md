vk-video
========
![текст](https://sun9-82.userapi.com/s/v1/if2/oJ68gg3NEQCB0OUXaiB1TuZjoXMrFVQ0iUAULZX0RP4NN6sDjog1hyXkncG-_y7u-xAYswzIuimHEZ6fOgyZpHE3.jpg?size=1196x400&quality=96&type=album)
- отправка видео командами
- основной шаблон - это все записи в [группе вк](https://vk.com/vk.video_userbot), которые может добавлять каждый
____
## установка
-     apt install git
-     git clone https://github.com/HANTER-NA-CODE/vk-video
### если вы устанавливаете в термуксе, то допишите вот это
-     cd vk-video
-     bash install-termux

## настройка
- первым делом нужно "сменить токен", для этого введи: `2`
- теперь вставь свой токен [как получить токен?](#как-получить-токен)
- далее нужно создать [шаблоны](#шаблоны)
____

## шаблоны
- вложение - id вложения, тоесть ссылка на видео/фото/документ, например

    https://vk.com/video-200042852_456239190
    
    нам нужно всё, что после `https://vk.com/`, тоесть `video-200042852_456239190`
- сообщение - текст сообщения, при котором сообщение поменяется на приклеплённое вложение
____
## как получить токен ##
- перейди по ссылке https://vkhost.github.io
- там выбери пункт `настройки`
- выбери нужные параметры

p.s. во избежание ошибок лучше выбрать все
- нажми `получить`
- затем `разрешить`
- скопируйте часть адресной строки от `access_token=` до `&expires_in`

     ![Alt-текст](https://sun9-39.userapi.com/impf/qf7ttaWiqX-JtP7vr3A7N_vk3GqN_-LO5WTEkQ/u_Oig4krD58.jpg?size=1179x56&quality=96&sign=f48c639fc76ab4f0e1aaa380db03cbbf&type=album)
