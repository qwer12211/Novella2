import time
def getattr(user):
    print("приветствуем  вас," + user)
getattr("Пользователь")
print("Павила игры:")
input()
def getatt(ise):
    print("Для прокручивания текста используйте клавишу:" + ise)
getatt("Enter")
print("Часть первая")
try:
    name = input("Введите имя персонажа: " )
    name = name.title()                                                                        #преобразование
    age = float(input("Введите возраст персонажа:"))
    info = "Имя вашего персонажа: %s, Возраст вашего персонажа: %d" % (name, age)                                                #форматирование строк
    print(info)
    input()
except ValueError:
    print("Ошибка")
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

itemsnarukzake = {"верёвка"}
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

input()

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

rukzak = {"батон хлеба", "ножик", "зажигалка"}
for i in rukzak:
    print(i)
    print("Лежит в вашем рюкзаке:")

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
print(textA.upper())                                                                        #преобразование строки на все заглавные

fraza = f"{name}, ты меня слышишь?"
print(fraza)

text = ("Кто вы?\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("Ещё недавно был Роджером Кортессом. Хотя, может, всё изменилось после того, как я умер.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

def getat(ie):
    print("Его имя:" + ie)
getat("Роджер Кортесс?!")


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

text = ("Вы понимаете, что убираться отсюда, пока не случилось ничего дурного.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

messege = ("Роджер: \" Куда же ты спешишь?.\n")
for char in messege:
     print(char, end='', flush=True)
     time.sleep(0.04)


text = ("Вы говорите, что родители учили вас не разговаривать с незнакомцами.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

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


text = ("Вы спрашиваете что ему от вас нужно.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

messege = ("Роджер: Я жажду мести. До сих пор никто из людей не видел и не слышал меня, но ты станешь моим голосом и руками. Я, наконец, смогу расправиться со своими убийцами, предавшими меня, и обрету покой!\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

print("Ты ошибаешься. Я ничем не смогу тебе помочь. Ты только зря тратишь время. – Ответили вы.")
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

print("А если я откажусь? – Ответили вы.")
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

text = (" Из кустов неосторожно вывалилось небольшая собака по кличке Виквик.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("Как бы мне ни хотелось это признавать, но - да, это мой домашний питомец.\n")
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

print("Конец первой части")

