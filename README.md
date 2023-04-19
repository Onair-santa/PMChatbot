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
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN","38928:G2y9Vo")  # Взять в боте @BotFather
    API_ID = int(os.environ.get("API_ID","123456789"))            # Взять(создать) на сайте https://my.telegram.org
    API_HASH = os.environ.get("API_HASH","cc1cd057a36901ff025")   # Взять(создать) на сайте https://my.telegram.org
    ADMIN = int(os.environ.get("ADMIN","123456789"))              # ID юзера, владельца бота. Посмотреть в @username_to_id_bot 
``` 
- Установить в папке виртуальное окружение и запустить
```
apt install virtualenv
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 bot.py
```
- Включение службы и автозапуска
```
cd /etc/systemd/system/
nano pmchat.service
```
[Unit]
Description=pmchat
After=network.target
[Service]
User=root
WorkingDirectory=/home/ME/pmchat
Environment="PYTHONPATH=/home/ME/pmchat/"
ExecStart=/home/ME/pmchat/venv/bin/python3 /home/ME/pmchat/bot.py --serve-in-foreground
RestartSec=10
Restart=always
[Install]
WantedBy=multi-user.target
```
```
sudo systemctl start pmchat
sudo systemctl stop pmchat
sudo systemctl restart pmchat
sudo systemctl status pmchat
```
# Команды пользователя бота
```
/start или /help - Приветствие
```
# Команды Админа
```
/info - Информация о пользователе
```

Благодарность
[m4mallu](https://github.com/m4mallu/PMChatbot)
