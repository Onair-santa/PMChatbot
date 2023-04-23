# 📥 PMChatBot 
Simple PM-bot
# 💠 Описание

- Users can pm to the bot via text or media messages
- Bot will send the message to the admin user id as pm.
- The replied message will be sent to the user as pm in the bot.

# Linux VPS:
- Rename sample_config.py в config.py and change config
```
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN","38928:G2y9Vo")  #  @BotFather
    API_ID = int(os.environ.get("API_ID","123456789"))            #  https://my.telegram.org
    API_HASH = os.environ.get("API_HASH","cc1cd057a36901ff025")   #  https://my.telegram.org
    ADMIN = int(os.environ.get("ADMIN","123456789"))              #  Owner ID  
``` 
- Virtual env
```
apt install virtualenv
virtualenv -p python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 bot.py
```
- Service
```
cd /etc/systemd/system/
nano pmchat.service
```
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
# Bot command
```
/start or /help 
```
# Admin command (not needed in my version of the bot)
```
/info
```

Credits
[m4mallu](https://github.com/m4mallu/PMChatbot)
