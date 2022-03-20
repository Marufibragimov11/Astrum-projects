Sonlar = {'1': ' ', '2': ' ', '3': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '7': ' ', '8': ' ', '9': ' '}

Kalit = []

for s in Sonlar:
    Kalit.append(s)


def printBoard(qator):
    print(qator['1'] + ' | ' + qator['2'] + ' | ' + qator['3'])
    print('---------')
    print(qator['4'] + ' | ' + qator['5'] + ' | ' + qator['6'])
    print('---------')
    print(qator['7'] + ' | ' + qator['8'] + ' | ' + qator['9'])


def oyin():
    xarf = 'X'
    a = 0
    for i in range(10):
        printBoard(Sonlar)
        print(xarf + " ni gali. Xo'sh qayerga yuramz?")
        k = input()
        if Sonlar[k] == ' ':
            Sonlar[k] = xarf
            a += 1
        else:
            print("Bu joy band.\nBoshqa katakcha tanlang")
            continue

        if a >= 5:
            if Sonlar['7'] == Sonlar['8'] == Sonlar['9'] != ' ':
                printBoard(Sonlar)
                print("\nG'olib aniqlandi. 🎉🎉🎉\n")
                print(" 🎉 " + xarf + " ni tabriklaymiz. 🎉")
                break
            elif Sonlar['4'] == Sonlar['5'] == Sonlar['6'] != ' ':
                printBoard(Sonlar)
                print("\nG'olib aniqlandi. 🎉🎉🎉\n")
                print(" 🎉 " + xarf + " ni tabriklaymiz. 🎉")
                break
            elif Sonlar['1'] == Sonlar['2'] == Sonlar['3'] != ' ':
                printBoard(Sonlar)
                print("\nG'olib aniqlandi. 🎉🎉🎉\n")
                print(" 🎉 " + xarf + " ni tabriklaymiz. 🎉")
                break
            elif Sonlar['1'] == Sonlar['4'] == Sonlar['7'] != ' ':
                printBoard(Sonlar)
                print("\nG'olib aniqlandi. 🎉🎉🎉\n")
                print(" 🎉 " + xarf + " ni tabriklaymiz. 🎉")
                break
            elif Sonlar['2'] == Sonlar['5'] == Sonlar['8'] != ' ':
                printBoard(Sonlar)
                print("\nG'olib aniqlandi. 🎉🎉🎉\n")
                print(" 🎉 " + xarf + " ni tabriklaymiz. 🎉")
                break
            elif Sonlar['3'] == Sonlar['6'] == Sonlar['9'] != ' ':
                printBoard(Sonlar)
                print("\nG'olib aniqlandi. 🎉🎉🎉\n")
                print(" 🎉 " + xarf + " ni tabriklaymiz. 🎉")
                break
            elif Sonlar['7'] == Sonlar['5'] == Sonlar['3'] != ' ':
                printBoard(Sonlar)
                print("\nG'olib aniqlandi. 🎉🎉🎉\n")
                print(" 🎉 " + xarf + " ni tabriklaymiz. 🎉")
                break
            elif Sonlar['1'] == Sonlar['5'] == Sonlar['9'] != ' ':
                printBoard(Sonlar)
                print("\nG'olib aniqlandi. 🎉🎉🎉\n")
                print(" 🎉 " + xarf + " ni tabriklaymiz. 🎉")
                break

        if a == 9:
            print("\nG'olib aniqlandi.\n")
            print("")

        if xarf == 'X':
            xarf = 'O'
        else:
            xarf = 'X'

    yukla = input("Yana o'ynashni xoxlaysizmi?(Xa/Yo'q)")
    if yukla == "Xa" or yukla == "Xa":
        for s in Kalit:
            Sonlar[s] = " "

        oyin()


if __name__ == "__main__":
    oyin()
