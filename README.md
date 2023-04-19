# 📥 PMChatBot 
Простой бот персональных сообщений
# 💠 Описание
Пользователи общаются с вами через бота, ваши данные скрыты и ответы приходят от бота.
Ваш личный чат не забивается ненужными контактами и сообщениями.
- Пользователи могут писать сообщения и присылать файлы.
- Admin отвечает в боте методом *Ответить* *reply to the message* 
- Команда `/info` - более полная информация о написавшем сообщение.(Admin Only)

# Linux VPS:
- Создать папку бота на сервере и скопировать туда файлы бота
- Переименовать sample_config.py в config.py и вставить свои данные токенов и ID владельца бота
```
    TG_BOT_TOKEN = "TG_BOT_TOKEN"  # Взять в боте @BotFather
    API_ID = API_ID                # Взять(создать) на сайте https://my.telegram.org
    API_HASH = "API_HASH"          # Взять(создать) на сайте https://my.telegram.org
    ADMIN = ID_OWNER               # ID юзера, владельца бота. Посмотреть в @username_to_id_bot 
``` 
- Установить в папке виртуальное окружение и запустить
```
apt install virtualenv
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 bot.py
```
```
# Команды пользователя
/start или /help - Приветствие
# Команды Админа
/info - Информация о пользователе
```

Благодарность
[m4mallu](https://github.com/m4mallu/PMChatbot)
