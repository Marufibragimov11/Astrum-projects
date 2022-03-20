mehmonlar = {"Ali": ['    11', 'lyuks'], "Vali": ['14', 'ekonom'], "Hasan": ['12', 'standart']}


def mehmonlar_royhati(mehmonlar):
    print("Ismi\tXonasi\tXona turi")
    print("___________________________")
    for key in mehmonlar:
        print(f"{key.title()}\t {mehmonlar[key][0]}\t\t{mehmonlar[key][1]}")


def remove(mehmonlar):
    while True:
        ism = input("Kimni ro'yhatdan chiqaramiz? ").lower()
        try:
            del mehmonlar[ism]
            print(ism.title(), "ro'yxatdan chiqarildi")
            break
        except:
            print("Bunday ismdagi mehmon yo'q ")


def mehmon_qoshish(mehmonlar):
    ismi = input("Tashrif buyuruvchimizning ismini kiriting: ").lower()
    while True:
        xonasi = input('Tanlagan xona raqamini kiriting: ')
        if xonasi not in list(sum_rooms(mehmonlar)):
            break
        else:
            print("Bu xonamiz xozircha band, iltimos boshqa xona tanlashini iltimos qilin :( ")

    turi = input('Xonalarning turini tanlang: \n'
                 'e - ekonom\n'
                 's - standart\n'
                 'l - lyuks\n')
    if turi == 'e':
        tarifi = 'ekonom'
    elif turi == 's':
        tarifi = 'standart'
    else:
        tarifi = 'lyuks'
    mehmonlar[ismi] = [xonasi, tarifi]
    print(f"{ismi.title()} bizni ro'yxatga qo'shildi")


def sum_rooms(mehmonlar):
    natija = []
    for n in mehmonlar:
        natija.append(mehmonlar[n][0])
    return natija


def buyruq():
    while True:
        print("\nAstrum mehmonxonasiga xush kelibsiz :)")
        kirit_son = input("Buyruqni tanlang: \n"
                          "1 - mehmon qo'shish \n"
                          "2 - mehmonni ro'yhatdan chiqarish \n"
                          "3 - mehmonlar ro'yhati \n"
                          "\n"
                          "0 - dasturdan chiqish")
        kirit_son = int(input(()))
        if kirit_son == 1:
            mehmon_qoshish(mehmonlar)
        elif kirit_son == 2:
            remove(mehmonlar)
        elif kirit_son == 3:
            mehmonlar_royhati(mehmonlar)
        else:
            break


buyruq()
