import telebot
import settings
from telebot import types
import json
import datetime
import random


def rando():
    y = 0
    f = True
    x = random.random()
    if x >= 0.35:
        f = True
    else:
        f = False
    if f:
        y = random.uniform(0, 7)
    else:
        y = random.uniform(-7, 0)
    return y


now = datetime.datetime.now()

bot = telebot.TeleBot(settings.token)

gachi = []

with open('gachi.txt', 'r') as fw:
    gachi = json.load(fw)

people = []
try:
    with open('people.txt', 'r') as fw:
        people = json.load(fw)

except:
    with open('people.txt', 'w') as fw:
        json.dump(people, fw)


@bot.message_handler(commands=['run'])
def first(message):
    b = []
    e = -1
    for f in people:
        b.append(f[0])
        if f[0] == message.from_user.id:
            e = b.index(f[0])
    if e == -1:
        people.append([message.from_user.id, 0, now.strftime("%d")])
        print(people)
        with open('people.txt', 'w') as fw:
            json.dump(people, fw)
        b = []
        for f in people:
            b.append(f[0])
            if f[0] == message.from_user.id:
                e = b.index(f[0])
    print(e)

    if people[e][2] != now.strftime("%d"):  # != now.strftime("%d")  False
        g = people[e][1]
        r = rando()
        g += r
        if g < 0:
            g = 0
        people[e][1] = g
        with open('people.txt', 'w') as fw:
            json.dump(people, fw)
        if r >= 0:
            bot.send_photo(message.chat.id, random.choice(gachi),
                           "@" + message.from_user.username + " " + random.choice(
                               ["Твоя пипирка выросла до %s сантиметров.😇" % round(g, 2),
                                "Продолжай в том же духе и твой причандал будут принимать за хвост. Тебе не кажется что %s сантиметров это перебор?🤩" % round(
                                    g, 2), ]))
        else:
            bot.send_photo(message.chat.id, random.choice(gachi),
                           "@" + message.from_user.username + " " + random.choice([
                                                                                      "Твое достоинство стало качественнее до %s сантиметров. С уменьшением размера качество растет, не правда ли?🤓" % round(
                                                                                          g, 2),
                                                                                      "Теперь у тебя будет меньше проблем на танцполе. Хозяйство величиной %s сантиметров позволит тебе танцевать свободнее." % round(
                                                                                          g, 2),
                                                                                      "Больше не всегда лучше. Так что когда у тебя %s сантиметровое хозяйство это не повод плакать.😉" % round(
                                                                                          g, 2)]))
    else:
        bot.send_photo(message.chat.id, random.choice(gachi),
                       "@" + message.from_user.username + " " + "ты уже голосовал сегодня , приходи завтра!😑")


"""
@bot.message_handler(content_types=['photo' , 'text'])
def rsds(message):
    print(message.photo[-1].file_id)
    gachi.append(message.photo[-1].file_id)
    with open('gachi.txt', 'w') as fw:
            json.dump(gachi, fw)
"""
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0, timeout=20000)