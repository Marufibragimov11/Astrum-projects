import json
import sys
from termcolor import colored
from prettytable import PrettyTable

name_input = ""
user_index = 0
file = "users.json"

with open(file) as fayl:
    users = json.load(fayl)

isHelp = True


def load_tests():
    global name_input, user_index, answer, isHelp
    fayl = "tests.json"

    with open(fayl) as file:
        fayl_json = json.load(file)

    quest = 1
    score = 0

    is_user = False
    for i in range(len(users)):
        if users[i]['name'] == name_input:
            is_user = True
            user_index = i
            break

    if is_user:
        for i in fayl_json:
            print(colored(f"\n Savol {quest}/10: {i['question']}", 'yellow'))  # [0]['key']
            print(f"a) {i['answers'][0]['key']} \n"
                  f"b) {i['answers'][1]['key']} \n"
                  f"c) {i['answers'][2]['key']} \n"
                  f"d) {i['answers'][3]['key']} \n"
                  " \n"
                  f"h - help \n"
                  "")
            answer = input("Javob: ")

            if answer == 'h' and isHelp:
                count_help = 0
                print(f"{i['question']}\n")
                for j in range(4):
                    if not i['answers'][j]['isTrue'] and count_help < 2:
                        count_help += 1
                        continue
                    print(chr(97 + j) + ')', i['answers'][j]['key'])
                isHelp = False
                count_help = 0
                answer = input("Javob: ")

            elif answer == 'h' and not isHelp:
                print(colored("Siz yordamdan foydalanib bo'ldingiz!!!", 'red'))
                print(colored(f"\n Savol {quest}/10: {i['question']}", 'blue'))  # [0]['key']
                print(f"a) {i['answers'][0]['key']} \n"
                      f"b) {i['answers'][1]['key']} \n"
                      f"c) {i['answers'][2]['key']} \n"
                      f"d) {i['answers'][3]['key']} \n"
                      " \n"
                      f"h - help \n"
                      "")
                answer = input("Javob: ")

            if i['answers'][0]['isTrue'] == True and answer == "a":
                print(colored("Javobingiz to'gri", 'green'))
                score += 1

            elif i['answers'][0]['isTrue'] == False and answer == "a":
                print(colored("Javobingiz noto'gri", 'red'))
                print(f"Siz bu o'yinda {score}/10 ball yig'dingiz \n")
                users[user_index]['game'] += 1
                with open("users.json", 'w') as userlar:
                    json.dump(users, userlar)
                return start_game()

            elif i['answers'][1]['isTrue'] == True and answer == "b":
                print(colored("Javobingiz to'gri", 'green'))
                score += 1

            elif i['answers'][1]['isTrue'] == False and answer == "b":
                print(colored("Javobingiz noto'gri", 'red'))
                print(f"Siz bu o'yinda {score}/10 ball yig'dingiz \n")
                users[user_index]['game'] += 1
                with open("users.json", 'w') as userlar:
                    json.dump(users, userlar)
                return start_game()

            elif i['answers'][2]['isTrue'] == True and answer == "c":
                print(colored("Javobingiz to'gri", 'green'))
                score += 1

            elif i['answers'][2]['isTrue'] == False and answer == "c":
                print(colored("Javobingiz noto'gri", 'red'))
                print(f"Siz bu o'yinda {score}/10 ball yig'dingiz \n")
                users[user_index]['game'] += 1
                with open("users.json", 'w') as userlar:
                    json.dump(users, userlar)
                return start_game()

            elif i['answers'][3]['isTrue'] == True and answer == "d":
                print(colored("Javobingiz to'gri", 'green'))
                score += 1

            elif i['answers'][3]['isTrue'] == False and answer == "d":
                print(colored("Javobingiz noto'gri", 'red'))
                print(f"Siz bu o'yinda {score}/10 ball yig'dingiz \n")
                users[user_index]['game'] += 1
                with open("users.json", 'w') as userlar:
                    json.dump(users, userlar)
                return start_game()

            else:
                print("Noto'g'ri qiymat kiritildi: ")
                return load_tests()

            if score == 10:
                print("Sizni tabriklaymiz, siz g'olibsiz \n")

                users[user_index]['game'] += 1
                with open("users.json", 'w') as userlar:
                    json.dump(users, userlar)
                return start_game()

            quest += 1

            if users[user_index]['score'] < score:
                users[user_index]['score'] = score


    else:
        users.append({
            "name": name_input,
            "game": 0,
            "score": 0
        })

        with open("users.json", 'w') as userlar:
            json.dump(users, userlar)

        return load_tests()

    with open("users.json", 'w') as score:
        json.dump(users, score)


def user_list():
    global users
    x = PrettyTable()

    x.field_names = ["  Name  ", " Played ", "Best score"]

    for i in range(len(users)):
        x.add_row([users[i]['name'], users[i]['game'], users[i]['score']])

    print(x)
    return start_game()


def start_game():
    global name_input
    print(colored("'Who wants to be a billionaire' o'yiniga xush kelibsiz!!! \n"
                  "Quyidagilardan birini tanlang: \n"
                  "1 - O'yinni boshlash \n"
                  "2 - Reyting \n"
                  " \n"
                  "0 - Dasturdan chiqish", 'blue'))

    game = int(input())
    if game == 1:
        print("Ismingizni kiriting: ")
        name_input = input()
        return load_tests()
    elif game == 2:
        return user_list()
    else:
        sys.exit()


start_game()
