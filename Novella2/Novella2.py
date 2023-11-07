import time
import json
import csv
def getattr(user):
    print("приветствуем  вас," + user)
getattr("Пользователь")
print("Павила игры:")

def getatt(ise):
    print("Для прокручивания текста используйте клавишу:" + ise)
getatt("Enter")
print("Часть первая")

def menu():
    print("Меню:")
    print("1. Выход")
    print("2. Удалить все сохраненные данные")
    print("3. Просмотреть сохраненные данные")

    choice = input("Введите номер действия: ")
    if choice == "1":
        exit()
    elif choice == "2":
        delete_data()
    elif choice == "3":
        view_data()
    else:
        print("Неправильный выбор. Попробуйте еще раз.")
        menu()

def view_data():
    data = load_data()
    if len(data) == 0:
        print("Нет сохраненных данных.")
    else:
        print("Сохраненные данные:")
        for item in data:
            print(f"Имя: {item['name']}, Возраст: {item['age']}")


def delete_data():
    confirmation = input("Вы уверены, что хотите удалить все сохраненные данные? (y/n): ")
    if confirmation.lower() == "y":
        save_data([])
        print("Все сохраненные данные удалены.")
    else:
        print("Отменено.")
    menu()

def save_data(data):
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

def load_data():
    try:
        with open('data.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

def update_csv(data):
    csv_data = []
    for item in data:
        csv_data.append([item['name'], str(item['age'])])

    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerows(csv_data)

name = input("Введите имя персонажа: ")
name = name.title()
age = float(input("Введите возраст персонажа: "))

data = load_data()

data.append({'name': name, 'age': age})

save_data(data)

update_csv(data)
def Tekst():
    print("Начало")
info = "Имя вашего персонажа: %s, Возраст вашего персонажа: %d" % (name, age)
print(info)
input()

text = ("Одной тёмной вы решаете сбежать посмотреть море.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

input()

text = ("Ночью из окна поместья Флорбелей показался ваш образ.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)
text = ("Вы скинули вниз наскоро связанную из простыней и одежды верёвку.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("Вы  стали спускаться в кустарники цветущих алых роз.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("Спустившись, вы срываете розу и прекрепляете к своему рюкзаку.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

itemsnarukzake = {"верёвка."}
itemsnarukzake.add ("цветок розы,")
print("Теперь весит на вашем рюкзаке:")
print(*itemsnarukzake)

text = ("Вокруг стояла идеальная тишина, и только время от времени из леса доносилось тяжёлое уханье совы.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

input()

text = ("Нужно было уходить отсюда поскорее, пока вас не заметили.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("Вы решаете отсидеться в своём любимом месте на берегу моря.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("Через некоторое время послышался звук бриза, а с севера потянул насыщенный свежестью, запах моря.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("Вы решаете посмотреть, что успели положить в рюкзак в спешке.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

print("Теперь лежит в вашем рюкзаке:")
rukzak = {"Батон хлеба", "Ножик", "Зажигалка."}
for i in rukzak:
    print(i)

text = ("Вы вошли в свою тайную обитель.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("На ровной глади моря отражались звёзды, напоминая шахту с изумрудными россыпями.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

input()

messege = ("Вдруг в темноте раздалось: \"Ещё одна заблудшая душа вышла подышать свежим воздухом?\n")
for char in messege:
     print(char, end='', flush=True)
     time.sleep(0.04)

textA = (" кто здесь?!\n")
print(textA.upper())

fraza = f"{name}, ты меня слышишь?"
print(fraza)

def gettra(saewr):
    print( saewr + "Кто вы?")
gettra("Вы: ")


text = ("Ещё недавно был Роджером Кортессом. Хотя, может, всё изменилось после того, как я умер.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

def getat(ie):
    print("Его имя:" + ie)
getat("Роджер Кортесс?!")

input()

text = ("Вам занкомо это имя.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)
input()

text = ("Им пугают детей на ночь. Только, в отличие от сказок, все те ужасы, что о нём рассказывают, правдивы.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("Он - самый безжалостный пират современности.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("Вы понимаете, что нужно убираться отсюда, пока не случилось ничего дурного.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

messege = ("Роджер: \" Куда же ты спешишь?.\n")
for char in messege:
     print(char, end='', flush=True)
     time.sleep(0.04)

def gettr(sewr):
    print( sewr + "Родители учили меня не разговаривать с незнакомцами.")
gettr("Вы: ")

input()

messege = ("Роджер: \" Ха-ха-ха!\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("Какой ужасающий смех\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

input()

messege = ("Роджер:Ты ведь понимаешь, что тебе так просто от меня не уйти?\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

def getatr(ser):
    print( ser + "Что тебе от  меня нужно?")
getatr("Вы: ")

input()

messege = ("Роджер: Я жажду мести. До сих пор никто из людей не видел и не слышал меня, но ты станешь моим голосом и руками. Я, наконец, смогу расправиться со своими убийцами, предавшими меня, и обрету покой!\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

def getar(se):
    print( se + "Ты ошибаешься. Я ничем не смогу тебе помочь. Ты только зря тратишь время")
getar("Вы: ")

input()

messege = ("Роджер:  Для меня время больше ничего не значит...\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("На минуту повисло молчание.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

messege = ("Роджер:  Хорошо, давай так: я предлагаю тебе сделку. Поможешь мне - и я скажу тебе, где перед смертью спрятал свои сокровища.\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

def getaptr(segr):
    print( segr + "А если я откажусь?")
getaptr("Вы: ")

input()

messege = ("Роджер:  Я сведу тебя с ума. У меня много свобоного времени и спешить мне некуда.\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("У вас не оставалось выбора кроме как согласиться.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

input()

text = ("Время тянулось ужасающе медленно.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("Вы же сидели на поросшем мхом камне, чувствуя под ногами промёрзший песок.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("Вдруг за спиной громко зашуршали кусты и стали ломаться ветки.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("Из кустов неосторожно вывалилось небольшая собака по кличке Вивик.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("Как бы  ни хотелось это признавать, но - да, это ваш домашний питомец.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

messege = ("Роджер:  Что это за отвратительное существо?\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

messege = ("Роджер:  Ладно, приходи сюда завтра ночью.\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

input()

text = (" ВЫ дожидались утра, раздумывая об этой встрече.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = (" С утра вы хотели первым делом направиться в торговый квартал на поиски вашего друга Ларса.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

menu()
