from universal_bankomat import languages

client_list = [
    {"card_number": "8600213216556156", "card_type": "Uzcard", "pin_code": "2266", "balance": 400000,
     "currency_type": "so'm", "card_status": True},
    {"card_number": "8600213216556112", "card_type": "Uzcard", "pin_code": "2266", "balance": 400000,
     "currency_type": "so'm", "card_status": True},
    {"card_number": "8600213216556134", "card_type": "Humo", "pin_code": "2266", "balance": 600000,
     "currency_type": "so'm", "card_status": True},
    {"card_number": "8600213216556114", "card_type": "Humo", "pin_code": "2266", "balance": 600000,
     "currency_type": "so'm", "card_status": True},
    {"card_number": "8600213216556116", "card_type": "Visa", "pin_code": "2266", "balance": 4000,
     "currency_type": "$", "card_status": True},
    {"card_number": "8600213216556154", "card_type": "Visa", "pin_code": "2266", "balance": 4000,
     "currency_type": "$", "card_status": True},
    {"card_number": "8600213216556157", "card_type": "Master", "pin_code": "2266", "balance": 4000,
     "currency_type": "$", "card_status": True},
    {"card_number": "8600213216556198", "card_type": "Master", "pin_code": "2266", "balance": 4000,
     "currency_type": "$", "card_status": True}
]


def getBalance(step_num, language, client, client_index):
    if language == "1" and step_num == 3:
        print(f"Sizning hisobingiz: {client[client_index]['balance']} {client[client_index]['currency_type']}")
    elif language == "2" and step_num == 3:
        print(f"Ваш счет: {client[client_index]['balance']} {client[client_index]['currency_type']}")
    elif language == "3" and step_num == 3:
        print(f"Your expense: {client[client_index]['balance']} {client[client_index]['currency_type']}")


def change_pin(language, client, client_index):
    if language == "2":
        new_pin = input("Введите новый пин-код: ")
        re_pin = input("Повторно введите новый пин-код: ")
        if new_pin == re_pin:
            print("Смена пин-кода прошла успешно!")
            client[client_index]["pin_code"] = new_pin

        else:
            print("Ошибка подтверждения пин-кода")
    elif language == "1":
        new_pin = input("Yangi pin kodni kiriting: ")
        re_pin = input("Yangi pin kodni qayta kiriting: ")
        if new_pin == re_pin:
            print("Pin kod almashtirish muvaffaqiyatli!")
            client[client_index]["pin_code"] = new_pin

        else:
            print("tasdiqlash pin kodi xato")
    else:
        new_pin = input("Enter the new pin code: ")
        re_pin = input("Re-enter the new pin code: ")
        if new_pin == re_pin:
            print("Pin code change successful!")
            client[client_index]["pin_code"] = new_pin

        else:
            print("Confirmation pin code error")


def withdraw_cash(language, client, client_index):
    if language == "1":
        withdraw = int(
            input(
                f"Miqdorni kiriting: max({client[client_index]['balance']} {client[client_index]['currency_type']}) "))
        if client[client_index]['balance'] >= withdraw:
            print("pul yechib olish amalga oshdi!!!")
            client[client_index]['balance'] -= withdraw

        else:
            print("Sizda yetarli mablag' mavjud emas")
    elif language == "2":
        withdraw = int(
            input(
                f"Введите сумму: max({client[client_index]['balance']} {client[client_index]['currency_type']}) "))
        if client[client_index]['balance'] >= withdraw:
            print("Вывод прошел успешно !!!")
            client[client_index]['balance'] -= withdraw

        else:
            print("У тебя не достаточно денег!!")
    else:
        withdraw = int(
            input(
                f"Enter the amount: max({client[client_index]['balance']} {client[client_index]['currency_type']}) "))
        if client[client_index]['balance'] >= withdraw:
            print("Withdrawal was successful !!!")
            client[client_index]['balance'] -= withdraw

        else:
            print("You don't have enough money!")


def deposit_cash(language, client, client_index):
    if language == "1":
        deposit = int(input("Balansizgizni qachaga to'ldirmoqchisiz: "))
        client[client_index]["balance"] += deposit
        print("To'lov amalga oshdi hisobingiz", client[client_index]['balance'], client[client_index]['currency_type'])
    elif language == "2":
        deposit = int(input("На сколько вы хотите пополнить баланс: "))
        client[client_index]["balance"] += deposit
        print("Ваш аккаунт оплачен", client[client_index]['balance'], client[client_index]['currency_type'])

    else:
        deposit = int(input("How much do you want to top up your balance: "))
        client[client_index]["balance"] += deposit
        print("Your account has been paid", client[client_index]['balance'], client[client_index]['currency_type'])


step = 0
isCard = False
index = 0
count_attempts = 0
card_pin = ''
lang = ''
card_number = ''
while True:
    if step == 0:
        if len(lang) > 0:
            step += 1
        else:
            lang = input("Tilni tanlang:\n"
                         "Выберите язык\n"
                         "Select the language\n"
                         "1. UZ\n"
                         "2. RU\n"
                         "3. ENG\n")
            step += 1

        if lang == '1' and step == 1:
            if len(card_number) > 0:
                step += 1
            else:
                card_number = input("Karta raqamini kiriting: (0-> orqaga) ")
                step += 1
                if card_number == "0":
                    step = 0
                    lang = ''
            for i in range(len(client_list)):
                if card_number == client_list[i]['card_number']:
                    index = i
                    isCard = True
                    break
            if isCard and step == 2:
                if client_list[index]["card_status"]:
                    if count_attempts <= 3:
                        if len(card_pin) > 0:
                            step += 1
                        else:
                            card_pin = input("Pin kodni kiriting ")
                            step += 1
                        if card_pin == client_list[index]["pin_code"] and step == 3:
                            count_attempts = 0

                            select_way = input("1. Balansni ko'rish\n"
                                               "2. Pul yechib olish\n"
                                               "3. Pul kiritish\n"
                                               "4. Pin kodni o'zgartirish\n"
                                               "5. Xizmatlardan foydalanish\n"
                                               "6. Orqaga qaytish\n"
                                               "7. Bosh sahifaga qaytish  \n")

                            if select_way == "1":
                                getBalance(step, lang, client_list, index)
                                step = 0
                            elif select_way == "2":
                                withdraw_cash(lang, client_list, index)
                                step = 0
                            elif select_way == "3":
                                deposit_cash(lang, client_list, index)
                                step = 0

                            elif select_way == "4":
                                change_pin(lang, client_list, index)
                                card_pin = client_list[index]["pin_code"]
                                step = 0
                            elif select_way == "5":
                                print("Xizmatlardan foydalanish")
                                languages()

                            elif select_way == "6":
                                step = 0
                                isCard = False
                                card_number = ''
                                card_pin = ''
                            elif select_way == "7":
                                lang = ''
                                card_number = ''
                                card_pin = ''
                                step = 0
                            else:
                                print("Berilganlardan birini tanlang!!")
                                step = 2
                        else:
                            count_attempts += 1
                            step = 0
                            card_pin = ''
                            if count_attempts == 3:
                                print("kartangiz bloklandi !")
                                client_list[index]['card_status'] = False
                                card_pin = ''
                                card_number = ''
                                lang = ''
                                step = 0
                                count_attempts = 0
                else:
                    count_attempts = 0
                    step = 0
                    print("kartangiz bloklagan !")
                    break
            elif not isCard and card_number != "0":
                print("Bunday karta mavjud emas")
                card_number = ''
                step = 0


        elif lang == '2' and step == 1:
            if len(card_number) > 0:
                step += 1
            else:
                card_number = input("Введите номер карты: (0-> назад)")
                step += 1
                if card_number == "0":
                    step = 0
                    lang = ''
            for i in range(len(client_list)):
                if card_number == client_list[i]['card_number']:
                    index = i
                    isCard = True
                    break
            if isCard and step == 2:
                if client_list[index]["card_status"]:
                    if count_attempts <= 3:
                        if len(card_pin) > 0:
                            step += 1
                        else:
                            card_pin = input("Введите ПИН-код: ")
                            step += 1
                        if card_pin == client_list[index]["pin_code"] and step == 3:
                            count_attempts = 0

                            select_way = input("1. Просмотреть баланс \n"
                                               "2. Снятие \n"
                                               "3. Депозит \n"
                                               "4. Изменить пин-код \n"
                                               "5. Использование услуг \n"
                                               "6. Назад \n"
                                               "7. Вернуться домой \n")

                            if select_way == "1":
                                getBalance(step, lang, client_list, index)
                                step = 0
                            elif select_way == "2":
                                withdraw_cash(lang, client_list, index)
                                step = 0
                            elif select_way == "3":
                                deposit_cash(lang, client_list, index)
                                step = 0
                            elif select_way == "4":
                                change_pin(lang, client_list, index)
                                card_pin = client_list[index]["pin_code"]
                                step = 0
                            elif select_way == "5":
                                print("Использование услуг")
                                languages()

                            elif select_way == "6":
                                step = 0
                                card_number = ''
                                card_pin = ''
                                isCard = False

                            elif select_way == "7":
                                lang = ''
                                card_number = ''
                                card_pin = ''
                                step = 0
                            else:
                                print("Выбери один из предложенных !!")
                                step = 0
                        else:
                            count_attempts += 1
                            step = 0
                            card_pin = ''
                            if count_attempts == 3:
                                print("Ваша карта заблокирована!")
                                client_list[index]['card_status'] = False
                                card_pin = ''
                                card_number = ''
                                lang = ''
                                step = 0
                                count_attempts = 0
                else:
                    count_attempts = 0
                    print("Ваша карта заблокирована!")
                    step = 0
                    break
            elif not isCard and card_number != "0":
                print("Такой карты нет")
                card_number = ''
                step = 0

        elif lang == '3' and step == 1:
            if len(card_number) > 0:
                step += 1
            else:
                card_number = input("Enter card number: (0-> cancel) ")
                step += 1
                if card_number == "0":
                    step = 0
                    lang = ''
            for i in range(len(client_list)):
                if card_number == client_list[i]['card_number']:
                    index = i
                    isCard = True
                    break
            if isCard and step == 2:
                if client_list[index]["card_status"]:
                    if count_attempts <= 3:
                        if len(card_pin) > 0:
                            step += 1
                        else:
                            card_pin = input("Enter PIN: ")
                            step += 1
                        if card_pin == client_list[index]["pin_code"] and step == 3:
                            count_attempts = 0

                            select_way = input("1. View balance \n"
                                               "2. Withdraw money \n"
                                               "3. Deposit \n"
                                               "4. Change pin code \n"
                                               "5. Using the services \n"
                                               "6. Back \n"
                                               "7. Return home \n")

                            if select_way == "1":
                                getBalance(step, lang, client_list, index)
                                step = 0
                            elif select_way == "2":
                                withdraw_cash(lang, client_list, index)
                                step = 0
                            elif select_way == "3":
                                deposit_cash(lang, client_list, index)
                                step = 0

                            elif select_way == "4":
                                change_pin(lang, client_list, index)
                                card_pin = client_list[index]["pin_code"]
                                step = 0
                            elif select_way == "5":
                                print("Use of services!")
                                languages()

                            elif select_way == "6":
                                step = 0
                                card_number = ''
                                card_pin = ''
                                isCard = False
                            elif select_way == "7":
                                lang = ''
                                card_number = ''
                                card_pin = ''
                                step = 0
                            else:
                                print("Choose one of the suggested ones !!")
                                step = 0
                        else:
                            count_attempts += 1
                            step = 0
                            card_pin = ''
                            if count_attempts == 3:
                                print("Your card is blocked!")
                                client_list[index]['card_status'] = False
                                card_pin = ''
                                card_number = ''
                                lang = ''
                                step = 0
                                count_attempts = 0
                else:
                    count_attempts = 0
                    print("Your card is blocked!!")
                    step = 0
                    break
            elif not isCard:
                print("There is no such card!")
                card_number = ''
                step = 0

        else:
            lang = ''
            step = 0

