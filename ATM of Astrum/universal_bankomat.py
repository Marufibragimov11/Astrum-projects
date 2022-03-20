from datetime import datetime

now = datetime.now()  # current date and time

date_time = now.strftime("%H:%M:%S")
date_year = now.strftime("%d-%m-%Y")

check = ("*****************************\n"
         "*        Error 404!         *\n"
         "*                           *\n"
         "*     To'langan vaqti:      *\n"
         f"*         {date_time}          *\n"
         f"*        {date_year}         *\n"
         "*                           *\n"
         "*       Call centre:        *\n"
         "*     +998 998 998 998      *\n"
         "*                           *\n"
         "*     To'lovingiz uchun     *\n"
         "*         raxmat!           *\n"
         "*                           *\n"
         "*    https://error404.uz    *\n"                                              
         "*****************************\n")

print("Error: 404! bankiga xush kelibsiz :)".center(150))
def languages():
    print("1 - O'zbek tili \n"
          "2 - Русский язык \n"
          "3 - English language")
    lang = int(input())
    if lang == 1:
        operations(lang)
    elif lang == 2:
        operations(lang)
    elif lang == 3:
        operations(lang)
    else:
        languages()

def operations(lang):
    if lang == 1:
        print("Quyidagilardan birini tanlang")
        print("1 - Mobil operatorlar \n"
              "2 - Internet provayderlar \n"
              "3 - IP telefoniya va TV \n"
              "4 - Kommunal to'lovlar \n"
              "5 - GAI \n"
              "6 - Transport \n"
              " \n"
              "0 - Ortga qaytish")
        uz_input = int(input())
        if uz_input == 1:
            mobile_operators(lang)
        elif uz_input == 2:
            internet(lang)
        elif uz_input == 3:
            telefoniya_tv(lang)
        elif uz_input == 4:
            communal(lang)
        elif uz_input == 5:
            ypx(lang)
        elif uz_input == 6:
            transport(lang)
        elif uz_input == 0:
            languages()
        else:
            print("Noto'g'ri buyruq kiritildi!!!")
            return operations(lang)

    elif lang == 2:
        print("Выберите один из следующих")
        print("1 - Мобильные операторы \n"
              "2 - Интернет-провайдеры \n"
              "3 - IP телефония и ТВ \n"
              "4 - Коммунальные платежи \n"
              "5 - ГАИ \n"
              "6 - Транспорт \n"
              " \n"
              "0 - назад")
        uz_input = int(input())
        if uz_input == 1:
            mobile_operators(lang)
        elif uz_input == 2:
            internet(lang)
        elif uz_input == 3:
            telefoniya_tv(lang)
        elif uz_input == 4:
            communal(lang)
        elif uz_input == 5:
            ypx(lang)
        elif uz_input == 6:
            transport(lang)
        elif uz_input == 0:
            languages()
        else:
            print("Введена неверная команда!!!")
            return operations(lang)

    elif lang == 3:
        print("Choose one of the following")
        print("1 - Mobile operators \n"
              "2 - Internet service providers \n"
              "3 - IP telephony and TV \n"
              "4 - Communal payments \n"
              "5 - Traffic police \n"
              "6 - Transport \n"
              " \n"
              "0 - back")
        uz_input = int(input())
        if uz_input == 1:
            mobile_operators(lang)
        elif uz_input == 2:
            internet(lang)
        elif uz_input == 3:
            telefoniya_tv(lang)
        elif uz_input == 4:
            communal(lang)
        elif uz_input == 5:
            ypx(lang)
        elif uz_input == 6:
            transport(lang)
        elif uz_input == 0:
            languages()
        else:
            print("Invalid command entered!!!")
            return operations(lang)
    else:
        return operations(lang)


# Mobil operatorlar uchun to'lov qismi


def mobile_operators(lang):
    if lang == 1:
        print("Operatorlardan birini tanlang! \n"
              "1 - MOBIUZ \n"
              "2 - Beeline \n"
              "3 - UzMobile \n"
              "4 - UCell \n"
              " \n"
              "0 - Ortga qaytish")
        choose = int(input())
        if choose == 1:
            mobiuz(lang)
        elif choose == 2:
            beeline(lang)
        elif choose == 3:
            UzMobile(lang)
        elif choose == 4:
            Ucell(lang)
        elif choose == 0:
            operations(lang)
        else:
            print("Noto'g'ri buyruq kiritildi!!!")
            return mobile_operators(lang)

    elif lang == 2:
        print("Выберите одного из операторов! \n"
              "1 - MOBIUZ \n"
              "2 - Beeline \n"
              "3 - UzMobile \n"
              "4 - UCell \n"
              " \n"
              "0 - назад")
        choose = int(input())
        if choose == 1:
            mobiuz(lang)
        elif choose == 2:
            beeline(lang)
        elif choose == 3:
            UzMobile(lang)
        elif choose == 4:
            Ucell(lang)
        elif choose == 0:
            operations(lang)
        else:
            print("Введена неверная команда!!!")
            return mobile_operators(lang)

    elif lang == 3:
        print("Choose one of the operators! \n"
              "1 - MOBIUZ \n"
              "2 - Beeline \n"
              "3 - UzMobile \n"
              "4 - UCell \n"
              " \n"
              "0 - back")
        choose = int(input())
        if choose == 1:
            mobiuz(lang)
        elif choose == 2:
            beeline(lang)
        elif choose == 3:
            UzMobile(lang)
        elif choose == 4:
            Ucell(lang)
        elif choose == 0:
            operations(lang)
        else:
            print("Invalid command entered!!!")
            return mobile_operators(lang)


def mobiuz(lang):
    if lang == 1:
        print("MOBIUZ ga hush kelibsiz! Kodlardan birini tanlang! \n"
              "1 - +99897 \n"
              "2 - +99888 \n"
              "\n"
              "3 - ortga qaytish \n"
              "0 - bosh sahifaga qaytish")
        code_number = int(input())
        if code_number == 1:
            print("+99897")
            checknumbers = input()
            if len(checknumbers) >= 8:
                print("Raqam noto'g'ri kiritldi!!! Iltimos qaytadan kiriting!!! ")
                return mobiuz(lang)
            else:
                print("To'lov summasini kiriting: ")
                payment_mobiuz = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_mobiuz = int(input())
                if check_mobiuz == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")
        elif code_number == 2:
            print("+99888")
            checknumbers = input()
            if len(checknumbers) >= 8:
                print("Raqam noto'g'ri kiritldi!!! Iltimos qaytadan kiriting!!! ")
                return mobiuz(lang)
            else:
                print("To'lov summasini kiriting: ")
                payment_mobiuz = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_mobiuz = int(input())
                if check_mobiuz == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")

        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Noto'g'ri buyruq kiritildi!!!")
            return mobiuz(lang)

    elif lang == 2:
        print("Добро пожаловать в MOBIUZ! \n"
              "1 - +99897 \n"
              "2 - +99888 \n"
              "\n"
              "3 - назад \n"
              "0 - Главная страница")
        code_number = int(input())
        if code_number == 1:
            print("+99897")
            checknumbers = input()
            if len(checknumbers) >= 8:
                print("Неправильно набран номер!!! Пожалуйста введите заново!!! ")
                return mobiuz(lang)
            else:
                print("Введите сумму платежа: ")
                payment_mobiuz = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_mobiuz = int(input())
                if check_mobiuz == 1:
                    print(check)
                else:
                    print("Спасибо, что были с нами :)")
        elif code_number == 2:
            print("+99888")
            checknumbers = input()
            if len(checknumbers) >= 8:
                print("Неправильно набран номер!!! Пожалуйста введите заново!!! ")
                return mobiuz(lang)
            else:
                print("Введите сумму платежа: ")
                payment_mobiuz = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_mobiuz = int(input())
                if check_mobiuz == 1:
                    print(check)
                else:
                    print("Спасибо, что были с нами :)")

        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Введена неверная команда!!!")
            return mobiuz(lang)

    elif lang == 3:
        print("Welcome to MOBIUZ! \n"
              "1 - +99897 \n"
              "2 - +99888 \n"
              "\n"
              "3 - Back \n"
              "0 - Home page")
        code_number = int(input())
        if code_number == 1:
            print("+99897")
            checknumbers = input()
            if len(checknumbers) >= 8:
                print("Wrong number dialed !!! Please re-enter!!! ")
                return mobiuz(lang)
            else:
                print("Enter payment amount: ")
                payment_mobiuz = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_mobiuz = int(input())
                if check_mobiuz == 1:
                    print(check)
                else:
                    print("Thank you for being with us :)")
        elif code_number == 2:
            print("+99888")
            checknumbers = input()
            if len(checknumbers) >= 8:
                print("Wrong number dialed !!! Please re-enter!!! ")
                return mobiuz(lang)
            else:
                print("Enter payment amount: ")
                payment_mobiuz = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_mobiuz = int(input())
                if check_mobiuz == 1:
                    print(check)
                else:
                    print("Thank you for being with us :)")

        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Invalid command entered!!!")
            return mobiuz(lang)


def beeline(lang):
    if lang == 1:
        print("Beeline ga hush kelibsiz! Kodlardan birini tanlang! \n"
              "<1> +99890 \n"
              "<2> +99891 \n"
              " \n"
              "3 - ortga qaytish \n"
              "0 - bosh sahifaga qaytish")
        code_number = int(input())
        if code_number == 1:
            print("+99890")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Raqam noto'g'ri kiritldi!!! Iltimos qaytadan kiriting!!! ")
                return beeline(lang)
            else:
                print("To'lov summasini kiriting: ")
                payment_beeline = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_beeline = int(input())
                if check_beeline == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")
        elif code_number == 2:
            print("+99891")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Raqam noto'g'ri kiritldi!!! Iltimos qaytadan kiriting!!! ")
                return beeline(lang)
            else:
                print("To'lov summasini kiriting: ")
                payment_beeline = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_beeline = int(input())
                if check_beeline == 1:
                    print(check)
                else:
                    print("Biz  bilan bo'lganingiz uchun raxmat :)")
        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Noto'g'ri buyruq kiritildi!!!")
            return beeline(lang)

    elif lang == 2:
        print("Добро пожаловать в Beeline!!! Выберите один из кодов! \n"
              "<1> +99890 \n"
              "<2> +99891 \n"
              " \n"
              "3 - назад \n"
              "0 - вернуться на главную страницу")
        code_number = int(input())
        if code_number == 1:
            print("+99890")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Номер был введен неверно!!! Пожалуйста, введите еще раз!!! ")
                return beeline(lang)
            else:
                print("Введите сумму платежа: ")
                payment_beeline = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_beeline = int(input())
                if check_beeline == 1:
                    print(check)
                else:
                    print("Спасибо, что были нами :)")
        elif code_number == 2:
            print("+99891")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Номер был введен неверно!!! Пожалуйста, введите еще раз!!! ")
                return beeline(lang)
            else:
                print("Введите сумму платежа: ")
                payment_beeline = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_beeline = int(input())
                if check_beeline == 1:
                    print(check)
                else:
                    print("Спасибо, что были нами :)")
        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Введена неверная команда!!!")
            return beeline(lang)

    elif lang == 3:
        print("Welcome to Beeline!!! Choose one of the codes! \n"
              "<1> +99890 \n"
              "<2> +99891 \n"
              " \n"
              "3 - back \n"
              "0 - Go back to main page")
        code_number = int(input())
        if code_number == 1:
            print("+99890")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("The number was entered incorrectly!!! Please enter again!!! ")
                return beeline(lang)
            else:
                print("Enter payment amount: ")
                payment_beeline = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_beeline = int(input())
                if check_beeline == 1:
                    print(check)
                else:
                    print("Thank you for being us :)")
        elif code_number == 2:
            print("+99891")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("The number was entered incorrectly!!! Please enter again!!! ")
                return beeline(lang)
            else:
                print("Enter payment amount: ")
                payment_beeline = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_beeline = int(input())
                if check_beeline == 1:
                    print(check)
                else:
                    print("Thank you for being us :)")
        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Invalid command entered!!!")
            return beeline(lang)


def UzMobile(lang):
    if lang == 1:
        print("UzMobile ga hush kelibsiz! Kodlardan birini tanlang! \n"
              "<1> +99895 \n"
              "<2> +99899 \n"
              " \n"
              "3 - ortga qaytish \n"
              "0 - bosh sahifaga qaytish")
        code_number = int(input())
        if code_number == 1:
            print("+99895")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Raqam noto'g'ri kiritldi!!! Iltimos qaytadan kiriting!!! ")
                return UzMobile(lang)
            else:
                print("To'lov summasini kiriting: ")
                payment_uzmobile = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_uzmobile = int(input())
                if check_uzmobile == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")
        elif code_number == 2:
            print("+99899")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Raqam noto'g'ri kiritldi!!! Iltimos qaytadan kiriting!!! ")
                return UzMobile(lang)
            else:
                print("To'lov summasini kiriting: ")
                payment_uzmobile = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_uzmobile = int(input())
                if check_uzmobile == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")

        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Noto'g'ri buyruq kiritildi!!!")
            return UzMobile(lang)

    elif lang == 2:
        print("Добро пожаловать в UzMobile! Выберите один из кодов! \n"
              "<1> +99895 \n"
              "<2> +99899 \n"
              " \n"
              "3 - назад \n"
              "0 - вернуться на главную страницу")
        code_number = int(input())
        if code_number == 1:
            print("+99895")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Номер был введен неверно!!! Пожалуйста, введите еще раз!!! ")
                return UzMobile(lang)
            else:
                print("Введите сумму платежа: ")
                payment_uzmobile = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_uzmobile = int(input())
                if check_uzmobile == 1:
                    print(check)
                else:
                    print("Спасибо, что были нами :)")
        elif code_number == 2:
            print("+99899")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Номер был введен неверно!!! Пожалуйста, введите еще раз!!! ")
                return UzMobile(lang)
            else:
                print("Введите сумму платежа: ")
                payment_uzmobile = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_uzmobile = int(input())
                if check_uzmobile == 1:
                    print(check)
                else:
                    print("Спасибо, что были нами :)")

        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Введена неверная команда!!!")
            return UzMobile(lang)

    elif lang == 3:
        print("Welcome to UzMobile! Choose one of the codes! \n"
              "<1> +99895 \n"
              "<2> +99899 \n"
              " \n"
              "3 - Back \n"
              "0 - Go back to main page")
        code_number = int(input())
        if code_number == 1:
            print("+99895")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("The number was entered incorrectly!!! Please enter again!!! ")
                return UzMobile(lang)
            else:
                print("Enter payment amount: ")
                payment_uzmobile = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_uzmobile = int(input())
                if check_uzmobile == 1:
                    print(check)
                else:
                    print("Thank you for being us :)")
        elif code_number == 2:
            print("+99899")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("The number was entered incorrectly!!! Please enter again!!! ")
                return UzMobile(lang)
            else:
                print("Enter payment amount: ")
                payment_uzmobile = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_uzmobile = int(input())
                if check_uzmobile == 1:
                    print(check)
                else:
                    print("Thank you for being us :)")

        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Invalid command entered!!!")
            return UzMobile(lang)

def Ucell(lang):
    if lang == 1:
        print("Ucell ga hush kelibsiz! Kodlardan birini tanlang! \n"
              "<1> +99893 \n"
              "<2> +99894 \n"
              " \n"
              "3 - ortga qaytish \n"
              "0 - bosh sahifaga qaytish")
        code_number = int(input())
        if code_number == 1:
            print("+99893")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Raqam noto'g'ri kiritldi!!! Iltimos qaytadan kiriting!!! ")
                return Ucell(lang)
            else:
                print("To'lov summasini kiriting: ")
                payment_ucell = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_ucell = int(input())
                if check_ucell == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")
        elif code_number == 2:
            print("+99894")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Raqam noto'g'ri kiritldi!!! Iltimos qaytadan kiriting!!! ")
                return UzMobile(lang)
            else:
                print("To'lov summasini kiriting: ")
                payment_ucell = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_ucell = int(input())
                if check_ucell == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")

        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Noto'g'ri buyruq kiritildi!!!")
            return Ucell(lang)

    if lang == 2:
        print("Добро пожаловать в Ucell! Выберите один из кодов! \n"
              "<1> +99893 \n"
              "<2> +99894 \n"
              " \n"
              "3 - назад \n"
              "0 - вернуться на главную страницу")
        code_number = int(input())
        if code_number == 1:
            print("+99893")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Номер был введен неверно!!! Пожалуйста, введите еще раз!!! ")
                return Ucell(lang)
            else:
                print("Введите сумму платежа: ")
                payment_ucell = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_ucell = int(input())
                if check_ucell == 1:
                    print(check)
                else:
                    print("Спасибо, что были нами :)")
        elif code_number == 2:
            print("+99894")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("Номер был введен неверно!!! Пожалуйста, введите еще раз!! ")
                return UzMobile(lang)
            else:
                print("Введите сумму платежа: ")
                payment_ucell = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_ucell = int(input())
                if check_ucell == 1:
                    print(check)
                else:
                    print("Спасибо, что были нами :)")

        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Введена неверная команда!!!")
            return Ucell(lang)

    if lang == 3:
        print("Welcome to Ucell! Choose one of the codes! \n"
              "<1> +99893 \n"
              "<2> +99894 \n"
              " \n"
              "3 - back \n"
              "0 - Go back to main page")
        code_number = int(input())
        if code_number == 1:
            print("+99893")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("The number was entered incorrectly!!! Please enter again!!! ")
                return Ucell(lang)
            else:
                print("Enter payment amount: ")
                payment_ucell = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_ucell = int(input())
                if check_ucell == 1:
                    print(check)
                else:
                    print("Thank you for being us :)")
        elif code_number == 2:
            print("+99894")
            checknumbers = int(input())
            if len(str(checknumbers)) >= 8:
                print("The number was entered incorrectly!!! Please enter again!! ")
                return UzMobile(lang)
            else:
                print("Enter payment amount: ")
                payment_ucell = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_ucell = int(input())
                if check_ucell == 1:
                    print(check)
                else:
                    print("Thank you for being us :)")

        elif code_number == 3:
            return mobile_operators(lang)
        elif code_number == 0:
            return operations(lang)
        else:
            print("Invalid command entered!!!")
            return Ucell(lang)


# Internet uchun to'lov qismi


def internet(lang):
    if lang == 1:
        print("Internet provayderlardan birini tanlang: \n"
              "1 - UzOnline \n"
              "2 - Sarkor Telecom \n"
              "3 - TPS \n"
              "4 - FiberNet \n"
              "5 - EVO + \n"
              " \n"
              "0 - Ortga qaytish")
        choose_inter = int(input())
        if choose_inter == 1:
            Uzonline(lang)
        elif choose_inter == 2:
            sarkor_telecom(lang)
        elif choose_inter == 3:
            tps(lang)
        elif choose_inter == 4:
            fibernet(lang)
        elif choose_inter == 5:
            evo(lang)
        elif choose_inter == 0:
            operations(lang)
        else:
            print("Noto'g'ri buyruq kiritildi!!! Iltimos qaytadan kiriting!!!")
            return internet(lang)

    elif lang == 2:
        print("Выберите одного из интернет-провайдеров: \n"
              "1 - UzOnline \n"
              "2 - Sarkor Telecom \n"
              "3 - TPS \n"
              "4 - FiberNet \n"
              "5 - EVO + \n"
              " \n"
              "0 - назад")
        choose_inter = int(input())
        if choose_inter == 1:
            Uzonline(lang)
        elif choose_inter == 2:
            sarkor_telecom(lang)
        elif choose_inter == 3:
            tps(lang)
        elif choose_inter == 4:
            fibernet(lang)
        elif choose_inter == 5:
            evo(lang)
        elif choose_inter == 0:
            operations(lang)
        else:
            print("Введен неправильный заказ !!! Пожалуйста, введите еще раз!!!")
            return internet(lang)

    elif lang == 3:
        print("Choose one of the internet providers: \n"
              "1 - UzOnline \n"
              "2 - Sarkor Telecom \n"
              "3 - TPS \n"
              "4 - FiberNet \n"
              "5 - EVO + \n"
              " \n"
              "0 - Back")
        choose_inter = int(input())
        if choose_inter == 1:
            Uzonline(lang)
        elif choose_inter == 2:
            sarkor_telecom(lang)
        elif choose_inter == 3:
            tps(lang)
        elif choose_inter == 4:
            fibernet(lang)
        elif choose_inter == 5:
            evo(lang)
        elif choose_inter == 0:
            operations(lang)
        else:
            print("Wrong order entered !!! Please enter again!!!")
            return internet(lang)


def Uzonline(lang):
    if lang == 1:
        print("Abonent hisob-raqamini kiriting: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Bunday hisob-raqam topilmadi!!! Iltimos tekshirib qaytadan kiriting!!!")
            return Uzonline(lang)
        else:
            print("To'lov summasini kiriting: ")
            pay_net_uz = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
                print("")
                languages()

    elif lang == 2:
        print("Войдите в аккаунт подписчика: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Такой учетной записи не найдено !!! Пожалуйста, проверьте и введите заново!!!")
            return Uzonline(lang)
        else:
            print("Введите сумму платежа: ")
            pay_net_uz = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Спасибо что были с нами")
                print("")
                languages()

    elif lang == 3:
        print("Sign in to your subscriber account: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("No such account found !!! Please check and re-enter!!!")
            return Uzonline(lang)
        else:
            print("Enter payment amount: ")
            pay_net_uz = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Thank you for being with us")
                print("")
                languages()

def sarkor_telecom(lang):
    if lang == 1:
        print("Abonent hisob-raqamini kiriting: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Bunday hisob-raqam topilmadi!!! Iltimos tekshirib qaytadan kiriting!!!")
            return sarkor_telecom(lang)
        else:
            print("To'lov summasini kiriting: ")
            pay_net_uz = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
                print("")
                languages()

    elif lang == 2:
        print("Войдите в аккаунт подписчика: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Такой учетной записи не найдено !!! Пожалуйста, проверьте и введите заново!!!")
            return sarkor_telecom(lang)
        else:
            print("Введите сумму платежа: ")
            pay_net_uz = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Спасибо что были с нами")
                print("")
                languages()

    elif lang == 3:
        print("Sign in to your subscriber account: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("No such account found !!! Please check and re-enter!!!")
            return sarkor_telecom(lang)
        else:
            print("Enter payment amount: ")
            pay_net_uz = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Thank you for being with us")
                print("")
                languages()

def tps(lang):
    if lang == 1:
        print("Abonent hisob-raqamini kiriting: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Bunday hisob-raqam topilmadi!!! Iltimos tekshirib qaytadan kiriting!!!")
            return tps(lang)
        else:
            print("To'lov summasini kiriting: ")
            pay_net_uz = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
                print("")
                languages()

    elif lang == 2:
        print("Войдите в аккаунт подписчика: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Такой учетной записи не найдено !!! Пожалуйста, проверьте и введите заново!!!")
            return tps(lang)
        else:
            print("Введите сумму платежа: ")
            pay_net_uz = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Спасибо что были с нами")
                print("")
                languages()

    elif lang == 3:
        print("Sign in to your subscriber account: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("No such account found !!! Please check and re-enter!!!")
            return tps(lang)
        else:
            print("Enter payment amount: ")
            pay_net_uz = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Thank you for being with us")
                print("")
                languages()

def fibernet(lang):
    if lang == 1:
        print("Abonent hisob-raqamini kiriting: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Bunday hisob-raqam topilmadi!!! Iltimos tekshirib qaytadan kiriting!!!")
            return fibernet(lang)
        else:
            print("To'lov summasini kiriting: ")
            pay_net_uz = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
                print("")
                languages()

    elif lang == 2:
        print("Войдите в аккаунт подписчика: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Такой учетной записи не найдено !!! Пожалуйста, проверьте и введите заново!!!")
            return fibernet(lang)
        else:
            print("Введите сумму платежа: ")
            pay_net_uz = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Спасибо что были с нами")
                print("")
                languages()

    elif lang == 3:
        print("Sign in to your subscriber account: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("No such account found !!! Please check and re-enter!!!")
            return fibernet(lang)
        else:
            print("Enter payment amount: ")
            pay_net_uz = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Thank you for being with us")
                print("")
                languages()

def evo(lang):
    if lang == 1:
        print("Abonent hisob-raqamini kiriting: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Bunday hisob-raqam topilmadi!!! Iltimos tekshirib qaytadan kiriting!!!")
            return evo(lang)
        else:
            print("To'lov summasini kiriting: ")
            pay_net_uz = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
                print("")
                languages()

    elif lang == 2:
        print("Войдите в аккаунт подписчика: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("Такой учетной записи не найдено !!! Пожалуйста, проверьте и введите заново!!!")
            return evo(lang)
        else:
            print("Введите сумму платежа: ")
            pay_net_uz = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Спасибо что были с нами")
                print("")
                languages()

    elif lang == 3:
        print("Sign in to your subscriber account: ")
        id_uz_input = int(input())
        if len(str(id_uz_input)) >= 8:
            print("No such account found !!! Please check and re-enter!!!")
            return evo(lang)
        else:
            print("Enter payment amount: ")
            pay_net_uz = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Thank you for being with us")
                print("")
                languages()

# IP telefoniya va tv uchun to'lov qismi


def telefoniya_tv(lang):
    if lang == 1:
        print("IP Telefoniya va TV bo'limiga xush kelibsiz :) \n"
              "1 - IP telefoniya \n"
              "2 - TV \n"
              " \n"
              "0 - Ortga qaytish")
        choose = int(input("Yuqoridagi buyruqlardan birini tanlang: "))
        if choose == 1:
            ip_telefoniya(lang)
        elif choose == 2:
            tv(lang)
        elif choose == 0:
            operations(lang)
        else:
            print("Noto'g'ri buyruq kiritildi!!!")
            return telefoniya_tv(lang)

    elif lang == 2:
        print("Добро пожаловать в раздел IP-телефония и ТВ :) \n"
              "1 - IP телефония \n"
              "2 - ТВ \n"
              " \n"
              "0 - назад")
        choose = int(input())
        if choose == 1:
            ip_telefoniya(lang)
        elif choose == 2:
            tv(lang)
        elif choose == 0:
            operations(lang)
        else:
            print("Введена неверная команда!!!")
            return telefoniya_tv(lang)

    elif lang == 3:
        print("Welcome to the section IP-telephony and TV :) \n"
              "1 - IP telephony \n"
              "2 - TV \n"
              " \n"
              "0 - Back")
        choose = int(input())
        if choose == 1:
            ip_telefoniya(lang)
        elif choose == 2:
            tv(lang)
        elif choose == 0:
            operations(lang)
        else:
            print("Invalid command entered!!!")
            return telefoniya_tv(lang)


def ip_telefoniya(lang):
    if lang == 1:
        print("Operatorlardan birini tanlang: \n"
              "1 - Shaxar telefoniyasi \n"
              "2 - Beeline \n"
              " \n"
              "3 - Ortga qaytish \n"
              "0 - Bosh sahifaga qaytish")
        operator = int(input())
        if operator == 1:
            print("Telefon raqamingizni kiriting: ")
            tel_number = int(input())
            print("To'lov summasini kiriting: ")
            pay_number = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
        elif operator == 2:
            print("Telefon raqamingizni kiriting: ")
            tel_number = int(input())
            print("To'lov summasini kiriting: ")
            pay_number = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
        elif operator == 3:
            telefoniya_tv(lang)
        elif operator == 0:
            operations(lang)
        else:
            print("Noto'g'ri buyruq kiritildi!!!")
            return ip_telefoniya(lang)

    elif lang == 2:
        print("Выберите одного из операторов: \n"
              "1 - Городская телефония \n"
              "2 - Beeline \n"
              " \n"
              "3 - назад \n"
              "0 - Возвращаться домой")
        operator = int(input())
        if operator == 1:
            print("Введите свой номер телефона: ")
            tel_number = int(input())
            print("Введите сумму платежа: ")
            pay_number = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
            else:
                print("Спасибо что были с нами ")
        elif operator == 2:
            print("Введите свой номер телефона: ")
            tel_number = int(input())
            print("Введите сумму платежа: ")
            pay_number = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
            else:
                print("Спасибо что были с нами")
        elif operator == 3:
            telefoniya_tv(lang)
        elif operator == 0:
            operations(lang)
        else:
            print("Введена неверная команда!!!")
            return ip_telefoniya(lang)

    elif lang == 3:
        print("Choose one of the operators: \n"
              "1 - City telephony \n"
              "2 - Beeline \n"
              " \n"
              "3 - back \n"
              "0 - Go back home")
        operator = int(input())
        if operator == 1:
            print("Enter your phone number: ")
            tel_number = int(input())
            print("Enter payment amount: ")
            pay_number = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
            else:
                print("Thank you for being with us ")
        elif operator == 2:
            print("Enter your phone number: ")
            tel_number = int(input())
            print("Enter payment amount: ")
            pay_number = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_ip = int(input())
            if check_ip == 1:
                print(check)
            else:
                print("Thank you for being with us")
        elif operator == 3:
            telefoniya_tv(lang)
        elif operator == 0:
            operations(lang)
        else:
            print("Invalid command entered!!!")
            return ip_telefoniya(lang)


def tv(lang):
    if lang == 1:
        print("Operatorlardan birini tanlang: \n"
              "1 - UzDigital TV \n"
              "2 - AllPlay \n"
              "3 - Sarkor TV \n"
              " \n"
              "4 - Ortga qaytish \n"
              "o - Bosh sahifaga qaytish")
        operator = int(input())
        if operator == 1:
            print("Abonent ID raqamini kiriting: ")
            id_raqam = int(input())
            print("To'lov summasini kiriting: ")
            pay_number = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_tv = int(input())
            if check_tv == 1:
                print(check)
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
        elif operator == 2:
            print("Abonent ID raqamini kiriting: ")
            id_raqam = int(input())
            print("To'lov summasini kiriting: ")
            pay_number = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_tv = int(input())
            if check_tv == 1:
                print(check)
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
        elif operator == 3:
            print("Abonent ID raqamini kiriting: ")
            id_raqam = int(input())
            print("To'lov summasini kiriting: ")
            pay_number = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_tv = int(input())
            if check_tv == 1:
                print(check)
            else:
                print("Biz bilan bo'lganingiz uchun raxmat")
        elif operator == 4:
            telefoniya_tv(lang)
        elif operator == 0:
            operations(lang)
        else:
            print("Noto'g'ri buyruq kiritildi!!!")
            return tv(lang)

    elif lang == 2:
        print("Выберите одного из операторов: \n"
              "1 - UzDigital TV \n"
              "2 - AllPlay \n"
              "3 - Sarkor TV \n"
              " \n"
              "4 - назад \n"
              "o - Вернуться на главную страницу")
        operator = int(input())
        if operator == 1:
            print("Введите идентификационный номер абонента: ")
            id_raqam = int(input())
            print("Введите сумму платежа: ")
            pay_number = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_tv = int(input())
            if check_tv == 1:
                print(check)
            else:
                print("Спасибо что были с нами")
        elif operator == 2:
            print("Введите идентификационный номер абонента: ")
            id_raqam = int(input())
            print("Введите сумму платежа: ")
            pay_number = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_tv = int(input())
            if check_tv == 1:
                print(check)
            else:
                print("Спасибо что были с нами")
        elif operator == 3:
            print("Введите идентификационный номер абонента: ")
            id_raqam = int(input())
            print("Введите сумму платежа: ")
            pay_number = int(input())
            print("Ваш платеж был успешно обработан!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_tv = int(input())
            if check_tv == 1:
                print(check)
            else:
                print("Спасибо что были с нами")
        elif operator == 4:
            telefoniya_tv(lang)
        elif operator == 0:
            operations(lang)
        else:
            print("Введена неверная команда!!!")
            return tv(lang)

    elif lang == 3:
        print("Choose one of the operators: \n"
              "1 - UzDigital TV \n"
              "2 - AllPlay \n"
              "3 - Sarkor TV \n"
              " \n"
              "4 - Back \n"
              "o - Go back to main page")
        operator = int(input())
        if operator == 1:
            print("Enter subscriber identification number: ")
            id_raqam = int(input())
            print("Enter payment amount: ")
            pay_number = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_tv = int(input())
            if check_tv == 1:
                print(check)
            else:
                print("Thank you for being with us")
        elif operator == 2:
            print("Enter subscriber identification number: ")
            id_raqam = int(input())
            print("Enter payment amount: ")
            pay_number = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_tv = int(input())
            if check_tv == 1:
                print(check)
            else:
                print("Thank you for being with us")

        elif operator == 3:
            print("Enter subscriber identification number: ")
            id_raqam = int(input())
            print("Enter payment amount: ")
            pay_number = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_tv = int(input())
            if check_tv == 1:
                print(check)
            else:
                print("Thank you for being with us")
        elif operator == 4:
            telefoniya_tv(lang)
        elif operator == 0:
            operations(lang)
        else:
            print("Invalid command entered!!!")
            return tv(lang)


# Kommunal uchun to'lov

def communal(lang):
    if lang == 1:
        print("Kommunal to'lovlardan birini tanlang: \n"
              "1 - Gaz \n"
              "2 - Svet \n"
              "3 - Suv \n"
              "4 - Musor \n"
              " \n"
              "0 - Ortga qaytish")
        komtolov = int(input())
        if komtolov == 1:
            gaz(lang)
        elif komtolov == 2:
            svet(lang)
        elif komtolov == 3:
            suv(lang)
        elif komtolov == 4:
            musor(lang)
        elif komtolov == 0:
            operations(lang)
        else:
            print("Noto'g'ri buyruq kitildi!!!")
            return communal(lang)
    elif lang == 2:
        print("Выберите один из счетов за коммунальные услуги: \n"
              "1 - Газ \n"
              "2 - Свет \n"
              "3 - Вода \n"
              "4 - Мусор \n"
              " \n"
              "0 - Назад")
        komtolov = int(input())
        if komtolov == 1:
            gaz(lang)
        elif komtolov == 2:
            svet(lang)
        elif komtolov == 3:
            suv(lang)
        elif komtolov == 4:
            musor(lang)
        elif komtolov == 0:
            operations(lang)
        else:
            print("Неправильно введена команда!!!")
            return communal(lang)

    elif lang == 3:
        print("Choose one of the utility bills: \n"
              "1 - Gas \n"
              "2 - Light \n"
              "3 - Water \n"
              "4 - Rubbish \n"
              " \n"
              "0 - Back")
        komtolov = int(input())
        if komtolov == 1:
            gaz(lang)
        elif komtolov == 2:
            svet(lang)
        elif komtolov == 3:
            suv(lang)
        elif komtolov == 4:
            musor(lang)
        elif komtolov == 0:
            operations(lang)
        else:
            print("Wrong command entered!!!")
            return communal(lang)


def gaz(lang):
    if lang == 1:
        print("Gazdagi abonent hisob-raqamingizni kiriting: ")
        gaz_uz = int(input())
        if len(str(gaz_uz)) >= 8:
            print("Abonent hisob-raqamingizni noto'g'ri kiritdingiz!!! Iltimos tekshirib qaytadan kiriting: ")
            return gaz(lang)
        else:
            print("To'lov summasini kiriting: ")
            gaz_pay = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_gaz = int(input())
            if check_gaz == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Biz bo'lganingiz uchun raxmat :)")
                print("")
                return languages()

    elif lang == 2:
        print("Введите свой аккаунт подписчика на газ: ")
        gaz_uz = int(input())
        if len(str(gaz_uz)) >= 8:
            print("Вы неправильно вошли в свой аккаунт подписчика!!! Пожалуйста, проверьте и введите заново: ")
            return gaz(lang)
        else:
            print("Введите сумму платежа: ")
            gaz_pay = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_gaz = int(input())
            if check_gaz == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Спасибо, что были нами :)")
                print("")
                return languages()

    elif lang == 3:
        print("Enter your gas subscriber account: ")
        gaz_uz = int(input())
        if len(str(gaz_uz)) >= 8:
            print("You are not logged into your subscriber account correctly!!! Please check and re-enter: ")
            return gaz(lang)
        else:
            print("Enter payment amount: ")
            gaz_pay = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_gaz = int(input())
            if check_gaz == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Thank you for being us :)")
                print("")
                return languages()


def svet(lang):
    if lang == 1:
        print("Svetdagi abonent hisob-raqamingizni kiriting: ")
        svet_uz = int(input())
        if len(str(svet_uz)) >= 8:
            print("Abonent hisob-raqamingizni noto'g'ri kiritdingiz!!! Iltimos tekshirib qaytadan kiriting: ")
            return svet(lang)
        else:
            print("To'lov summasini kiriting: ")
            svet_pay = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_svet = int(input())
            if check_svet == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Biz bo'lganingiz uchun raxmat :)")
                print("")
                return languages()

    elif lang == 2:
        print("Войдите в свой аккаунт подписчика в Свете: ")
        svet_uz = int(input())
        if len(str(svet_uz)) >= 8:
            print("Вы неправильно вошли в свой аккаунт подписчика!!! Пожалуйста, проверьте и введите заново: ")
            return svet(lang)
        else:
            print("Введите сумму платежа: ")
            svet_pay = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_svet = int(input())
            if check_svet == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Спасибо, что были нами :)")
                print("")
                return languages()

    elif lang == 3:
        print("Log in to your Subscriber account in Light: ")
        svet_uz = int(input())
        if len(str(svet_uz)) >= 8:
            print("You are not logged into your subscriber account correctly!!! Please check and re-enter: ")
            return svet(lang)
        else:
            print("Enter payment amount: ")
            svet_pay = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_svet = int(input())
            if check_svet == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Thank you for being us :)")
                print("")
                return languages()


def suv(lang):
    if lang == 1:
        print("Suvdagi abonent hisob-raqamingizni kiriting: ")
        suv_uz = int(input())
        if len(str(suv_uz)) >= 8:
            print("Abonent hisob-raqamingizni noto'g'ri kiritdingiz!!! Iltimos tekshirib qaytadan kiriting: ")
            return suv(lang)
        else:
            print("To'lov summasini kiriting: ")
            suv_pay = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_suv = int(input())
            if check_suv == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Biz bo'lganingiz uchun raxmat :)")
                print("")
                return languages()

    elif lang == 2:
        print("Войдите в свой аккаунт подписчика на воде: ")
        suv_uz = int(input())
        if len(str(suv_uz)) >= 8:
            print("Вы неправильно вошли в свой аккаунт подписчика!!! Пожалуйста, проверьте и введите заново: ")
            return suv(lang)
        else:
            print("Введите сумму платежа: ")
            suv_pay = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_suv = int(input())
            if check_suv == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Спасибо, что были нами :)")
                print("")
                return languages()

    elif lang == 3:
        print("Log in to your subscriber account on the water: ")
        suv_uz = int(input())
        if len(str(suv_uz)) >= 8:
            print("You have entered your subscriber account incorrectly !!! Please check and re-enter: ")
            return suv(lang)
        else:
            print("Enter payment amount: ")
            suv_pay = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_suv = int(input())
            if check_suv == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Thank you for being us :)")
                print("")
                return languages()


def musor(lang):
    if lang == 1:
        print("Musordagi abonent hisob-raqamingizni kiriting: ")
        musor_uz = int(input())
        if len(str(musor_uz)) >= 8:
            print("Abonent hisob-raqamingizni noto'g'ri kiritdingiz!!! Iltimos tekshirib qaytadan kiriting: ")
            return musor(lang)
        else:
            print("To'lov summasini kiriting: ")
            musor_pay = int(input())
            print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "To'lovingiz muvaffaqiyatli amalga oshirildi")
            print("Chek chiqarilsinmi??? \n"
                  "1 - Xa \n"
                  "2 - Yo'q")
            check_musor = int(input())
            if check_musor == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Biz bo'lganingiz uchun raxmat :)")
                print("")
                return languages()

    elif lang == 2:
        print("Войдите в свой аккаунт подписчика в Musor: ")
        musor_uz = int(input())
        if len(str(musor_uz)) >= 8:
            print("Вы неправильно вошли в свой аккаунт подписчика !!! Пожалуйста, проверьте и введите заново: ")
            return musor(lang)
        else:
            print("Введите сумму платежа: ")
            musor_pay = int(input())
            print("Подождите, пока ваш платеж обрабатывается!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Ваш платеж был успешно обработан")
            print("Выпустить чек??? \n"
                  "1 - Дa \n"
                  "2 - Нет")
            check_musor = int(input())
            if check_musor == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Спасибо, что были нами :)")
                print("")
                return languages()

    elif lang == 3:
        print("Log in to your Musor subscriber account: ")
        musor_uz = int(input())
        if len(str(musor_uz)) >= 8:
            print("You have entered your subscriber account incorrectly !!! Please check and re-enter: ")
            return musor(lang)
        else:
            print("Enter payment amount: ")
            musor_pay = int(input())
            print("Wait while your payment is being processed!!! \n"
                  "🔄 \n"
                  "🔄 \n"
                  "🔄 \n"
                  "Your payment has been successfully processed")
            print("Issue a check??? \n"
                  "1 - Yes \n"
                  "2 - No")
            check_musor = int(input())
            if check_musor == 1:
                print(check)
                print("")
                return languages()
            else:
                print("Thank you for being us :)")
                print("")
                return languages()


# GAI uchun to'lov qismi

def ypx(lang):
    if lang == 1:
        print("YPX bo'limiga xush kelibsiz \n"
              "ID raqamingizni kiriting: \n"
              " \n"
              "0 - Ortga qaytish")
        id_gai = int(input())
        if id_gai == 0:
            return operations(lang)
        else:
            if len(str(id_gai)) >= 8:
                print("ID raqamingizni noto'g'ri kiritdingiz!!! Iltimos tekshirib qaytadan kiriting: ")
                return ypx(lang)
            else:
                print("To'lov summasini kiriting: ")
                gai_pay = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_gai = int(input())
                if check_gai == 1:
                    print(check)
                    print("")
                    return languages()
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")
                    print("")
                    return languages()

    if lang == 2:
        print("Добро пожаловать в отдел YPX \n"
              "Введите свой идентификационный номер: \n"
              " \n"
              "0 - назад")
        id_gai = int(input())
        if id_gai == 0:
            return operations(lang)
        else:
            if len(str(id_gai)) >= 8:
                print("Вы неправильно ввели свой идентификационный номер !!! Пожалуйста, проверьте и введите заново: ")
                return ypx(lang)
            else:
                print("Введите сумму платежа: ")
                gai_pay = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_gai = int(input())
                if check_gai == 1:
                    print(check)
                    print("")
                    return languages()
                else:
                    print("Спасибо, что были нами :)")
                    print("")
                    return languages()

    if lang == 3:
        print("Welcome to the YPX department \n"
              "Enter your ID: \n"
              " \n"
              "0 - Back")
        id_gai = int(input())
        if id_gai == 0:
            return operations(lang)
        else:
            if len(str(id_gai)) >= 8:
                print("You entered your ID incorrectly !!! Please check and re-enter: ")
                return ypx(lang)
            else:
                print("Enter payment amount: ")
                gai_pay = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_gai = int(input())
                if check_gai == 1:
                    print(check)
                    print("")
                    return operations(lang)
                else:
                    print("Thank you for being us :)")
                    print("")
                    return operations(lang)


# transport uchun to'lov qismi


def transport(lang):
    if lang == 1:
        print("Transport turini tanlang: \n"
              "1- Yandex taxi \n"
              "2- Mytaxi \n"
              "3- Indriver \n"
              "4- ATTO \n"
              " \n"
              "0 - Ortga qaytish")

        transporta = int(input())
        if transporta == 1:
            yandex(lang)
        elif transporta == 2:
            mytaxi(lang)
        elif transporta == 3:
            INDRIVER(lang)
        elif transporta == 4:
            ATTO(lang)
        elif transporta == 0:
            operations(lang)
        else:
            print("Noto'g'ri son kiritildi!!!")
            return transport(lang)

    elif lang == 2:
        print("Выберите вид транспорта: \n"
              "1- Yandex taxi \n"
              "2- Mytaxi \n"
              "3- Indriver \n"
              "4- ATTO \n"
              " \n"
              "0 - назад")

        transporta = int(input())
        if transporta == 1:
            yandex(lang)
        elif transporta == 2:
            mytaxi(lang)
        elif transporta == 3:
            INDRIVER(lang)
        elif transporta == 4:
            ATTO(lang)
        elif transporta == 0:
            operations(lang)
        else:
            print("Введен неправильный номер!!!")
            return transport(lang)

    elif lang == 3:
        print("Choose a mode of transport: \n"
              "1- Yandex taxi \n"
              "2- Mytaxi \n"
              "3- Indriver \n"
              "4- ATTO \n"
              " \n"
              "0 - Back")

        transporta = int(input())
        if transporta == 1:
            yandex(lang)
        elif transporta == 2:
            mytaxi(lang)
        elif transporta == 3:
            INDRIVER(lang)
        elif transporta == 4:
            ATTO(lang)
        elif transporta == 0:
            operations(lang)
        else:
            print("Wrong number entered!!!")
            return transport(lang)


def yandex(lang):
    if lang == 1:
        print("Buyurtma raqamini kiriting: \n"
              " \n"
              "0 - Ortga qaytish")
        yandex_taxi = int(input())
        if yandex_taxi == 0:
            return transport(lang)
        else:
            if len(str(yandex_taxi)) >= 8:
                print("Buyurtma raqamini to'g'ri kiriting: ")
                return yandex(lang)
            else:
                print("To'lov summasini kiriting: ")
                pay_yandex = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_yandex = int(input())
                if check_yandex == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")

    elif lang == 2:
        print("Введите номер заказа: \n"
              " \n"
              "0 - назад")
        yandex_taxi = int(input())
        if yandex_taxi == 0:
            return transport(lang)
        else:
            if len(str(yandex_taxi)) >= 8:
                print("Введите номер заказа правильно: ")
                return yandex(lang)
            else:
                print("Введите сумму платежа: ")
                pay_yandex = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_yandex = int(input())
                if check_yandex == 1:
                    print(check)
                else:
                    print("Спасибо, что были нами :)")

    elif lang == 3:
        print("Enter your order number: \n"
              " \n"
              "0 - Back")
        yandex_taxi = int(input())
        if yandex_taxi == 0:
            return transport(lang)
        else:
            if len(str(yandex_taxi)) >= 8:
                print("Enter your order number correctly: ")
                return yandex(lang)
            else:
                print("Enter payment amount: ")
                pay_yandex = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_yandex = int(input())
                if check_yandex == 1:
                    print(check)
                else:
                    print("Thank you for being us :)")


def mytaxi(lang):
    if lang == 1:
        print("Buyurtma raqamini kiriting: \n"
              " \n"
              "0 - Ortga qaytish")
        mytaxip = int(input())
        if mytaxip == 0:
            return transport(lang)
        else:
            if len(str(mytaxi)) >= 8:
                print("Buyurtma raqamini to'g'ri kiriting: ")
                return mytaxi(lang)
            else:
                print("To'lov summasini kiriting: ")
                pay_mytaxi = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_mytaxi = int(input())
                if check_mytaxi == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")

    elif lang == 2:
        print("Введите номер заказа: \n"
              " \n"
              "0 - назад")
        mytaxip = int(input())
        if mytaxip == 0:
            return transport(lang)
        else:
            if len(str(mytaxi)) >= 8:
                print("Введите номер заказа правильно: ")
                return mytaxi(lang)
            else:
                print("Введите сумму платежа: ")
                pay_mytaxi = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_mytaxi = int(input())
                if check_mytaxi == 1:
                    print(check)
                else:
                    print("Спасибо, что были нами :)")

    elif lang == 3:
        print("Enter your order number: \n"
              " \n"
              "0 - Back")
        mytaxip = int(input())
        if mytaxip == 0:
            return transport(lang)
        else:
            if len(str(mytaxi)) >= 8:
                print("Enter your order number correctly: ")
                return mytaxi(lang)
            else:
                print("Enter payment amount: ")
                pay_mytaxi = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_mytaxi = int(input())
                if check_mytaxi == 1:
                    print(check)
                else:
                    print("Thank you for being us :)")


def INDRIVER(lang):
    if lang == 1:
        print("Buyurtma raqamini kiriting: \n"
              " \n"
              "0 - Ortga qaytish")
        indriver = int(input())
        if mytaxi == 0:
            return transport(lang)
        else:
            if len(str(indriver)) >= 8:
                print("Buyurtma raqamini to'g'ri kiriting: ")
                return INDRIVER(lang)
            else:
                print("To'lov summasini kiriting: ")
                tolov_indriver = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_indriver = int(input())
                if check_indriver == 1:
                    print(check)
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")

    elif lang == 2:
        print("Введите номер заказа: \n"
              " \n"
              "0 - назад")
        indriver = int(input())
        if mytaxi == 0:
            return transport(lang)
        else:
            if len(str(indriver)) >= 8:
                print("Введите номер заказа правильно: ")
                return INDRIVER(lang)
            else:
                print("Введите сумму платежа: ")
                tolov_indriver = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_indriver = int(input())
                if check_indriver == 1:
                    print(check)
                else:
                    print("Спасибо, что были нами :)")

    elif lang == 3:
        print("Enter your order number: \n"
              " \n"
              "0 - Back")
        indriver = int(input())
        if mytaxi == 0:
            return transport(lang)
        else:
            if len(str(indriver)) >= 8:
                print("Enter your order number correctly: ")
                return INDRIVER(lang)
            else:
                print("Enter payment amount: ")
                tolov_indriver = int(input())
                print("Wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_indriver = int(input())
                if check_indriver == 1:
                    print(check)
                else:
                    print("Thank you for being us :)")


def ATTO(lang):
    if lang == 1:
        print("ATTO karta raqamingizni kiriting: \n"
              " \n"
              "0 - Ortga qaytish")
        atto = int(input())
        if atto == 0:
            return transport(lang)
        else:
            if len(str(atto)) >= 17:
                print(len(str("ATTO karta raqamingizni to'g'ri kiriting: ")))
                return ATTO(lang)
            else:
                print("To'lov summasini kiriting: ")
                pay_atto = int(input())
                print("To'lovingiz amalga oshirilmoqda iltimos kuting!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "To'lovingiz muvaffaqiyatli amalga oshirildi")
                print("Chek chiqarilsinmi??? \n"
                      "1 - Xa \n"
                      "2 - Yo'q")
                check_atto = int(input())
                if check_atto == 1:
                    print(check)
                    print("")
                    return languages()
                else:
                    print("Biz bo'lganingiz uchun raxmat :)")
                    print("")
                    return languages()

    elif lang == 2:
        print("Введите номер вашей карты ATTO: \n"
              " \n"
              "0 - назад")
        atto = int(input())
        if atto == 0:
            return transport(lang)
        else:
            if len(str(atto)) >= 17:
                print(len(str("Правильно введите номер своей карты ATTO: ")))
                return ATTO(lang)
            else:
                print("Введите сумму платежа: ")
                pay_atto = int(input())
                print("Подождите, пока ваш платеж обрабатывается!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Ваш платеж был успешно обработан")
                print("Выпустить чек??? \n"
                      "1 - Дa \n"
                      "2 - Нет")
                check_atto = int(input())
                if check_atto == 1:
                    print(check)
                    print("")
                    return languages()
                else:
                    print("Спасибо, что были нами :)")
                    print("")
                    return languages()

    elif lang == 3:
        print("Enter your ATTO card number: \n"
              " \n"
              "0 - Back")
        atto = int(input())
        if atto == 0:
            return transport(lang)
        else:
            if len(str(atto)) >= 17:
                print(len(str("Enter your ATTO card number correctly: ")))
                return ATTO(lang)
            else:
                print("Enter payment amount: ")
                pay_atto = int(input())
                print("Please wait while your payment is being processed!!! \n"
                      "🔄 \n"
                      "🔄 \n"
                      "🔄 \n"
                      "Your payment has been successfully processed")
                print("Issue a check??? \n"
                      "1 - Yes \n"
                      "2 - No")
                check_atto = int(input())
                if check_atto == 1:
                    print(check)
                    print("")
                    return languages()
                else:
                    print("Thank you for being us :)")
                    print("")
                    return languages()


# operations()
