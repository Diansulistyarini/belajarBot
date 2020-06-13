import telebot
import mysql.connector

import mytoken


from datetime import datetime
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_belajarbot')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang=datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        # photo = open('img/rpl.png', 'rb')
        # myBot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA + "\n-- admin & developer @diansulistyarini - SMK Taruna Bhakti -- "+"\n" \
                        "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query="select nipd,nama,kelas from tabel_siswa "
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        datacollect=''
        if(jmldata>0):
            #print(data)
            no=0
            for x in data:
                no += 1
                datacollect =datacollect+ str(x)
                print(datacollect)
                datacollect = datacollect.replace('(', '')
                datacollect = datacollect.replace(')', '')
                datacollect = datacollect.replace("'", '')
                datacollect = datacollect.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(datacollect))

print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)
