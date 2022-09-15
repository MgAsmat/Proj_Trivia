import sys
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BOLD = '\033[1m'
RESET = '\033[39m'
END = '\033[0m'


def type(text):
    words = text
    for char in words:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()


begin_trivia = True
tries = 0

type(BLUE + "Welcome to language trivia (⁠＾⁠ ⁠〰⁠ ⁠＾⁠)\n" + RESET)
name = input("What's your name? : ")
print("\nHi " + name)

while begin_trivia == True:
    tries += 1
    pts = 0
    print("\nThis is your try Nº", tries)

    type("\nType a letter and press Enter to check your answer\n")

    type("\nYou have: ")
    print(pts, "points for now")

    type("\nNow let's start!\n")

    def function(kanji, a, b, c, d):
        print("\nWhat does " + kanji + " mean\n\n" + "a. " + a + "\nb. " + b +
              "\nc. " + c + "\nd. " + d)

    function("人", "Man", "Fire", "Enter", "Person")

    respuesta_1 = input("\nMy answer is: ")

    def func_ans(answer, correct, question):
        print(
            RED + "\nNope!\n" + answer + " is " +
            correct + "\nThe correct answer is " + question + ". You have",
            int(pts), "points" + RESET)

    while respuesta_1 not in ("a", "A", "b", "B", "c", "C", "d", "D"):
        respuesta_1 = input(
            YELLOW +
            "\nYou must answer either a, b, c or d. Type your answer again: " +
            RESET)
    if respuesta_1 in ("a", "A"):
        func_ans("Man", "男", "Person")
    elif respuesta_1 in ("b", "B"):
        func_ans("Fire", "火", "Person")
    elif respuesta_1 in ("c", "C"):
        func_ans("Enter", "入", "Person")
    else:
        pts += 2
        print(GREEN + "\nCorrect!\nYou have", pts, "points now" + RESET)
    time.sleep(1)

    print("\n")
    type("Next question!")
    print("\n")

    function("日", "Moon", "Day", "Eye", "Mouth")

    respuesta_2 = input("\nMy answer is: ")

    while respuesta_2 not in ("a", "A", "b", "B", "c", "C", "d", "D"):
        respuesta_2 = input(
            YELLOW +
            "\nYou must answer either a, b, c or d. Type your answer again: " +
            YELLOW)
    if respuesta_2 in ("a", "A"): func_ans("Moon", "月", "Day")
    elif respuesta_2 in ("c", "C"): func_ans("Eye", "目", "Day")
    elif respuesta_2 in ("d", "D"): func_ans("Mouth", "口", "Day")
    else:
        pts += 2
        print(GREEN + "\nCorrect!\nYou have", pts, "points now" + RESET)
    time.sleep(1)

    print("\n")
    type("Next question!")
    print("\n")

    function("水", "Water", "Ice", "Tree", "Book")

    respuesta_3 = input("\nMy answer is: ")

    while respuesta_3 not in ("a", "A", "b", "B", "c", "C", "d", "D"):
        respuesta_3 = input(
            YELLOW +
            "\nYou must answer either a, b, c or d. Type your answer again: " +
            RESET)
    if respuesta_3 in ("b", "B"): func_ans("Ice", "氷", "Water")
    elif respuesta_3 in ("c", "C"): func_ans("Tree", "木", "Water")
    elif respuesta_3 in ("d", "D"): func_ans("Book", "本", "Water")
    else:
        pts += 2
        print(GREEN + "\nCorrect!\nYou have", pts, "points now" + RESET)

    time.sleep(1)

    type("\nWant to double your points?\n")
    type(MAGENTA + "If you get it wrong you'll lose half your points\n" +
         RESET)
    if pts == 0:
        type(BLUE + "\nRemember! " + BOLD + "2 × 0 = 0 " + END + BLUE +
             "ಥ⁠‿⁠ಥ" + RESET)
    type("\nPress Y to continue or any other key to finish the game: ")

    challenge = input()

    if challenge in ("Y", "y"):
        print("\n")
        type(CYAN + "Bonus question!" + RESET)
        print("\n")
        function("白", "Oneself", "Day", "White", "One hundred")
        respuesta_4 = input("\nMy answer is: ")
        while respuesta_4 not in ("a", "A", "b", "B", "c", "C", "d", "D"):
            respuesta_4 = input(
                YELLOW +
                "\nYou must answer either a, b, c or d. Type your answer again: "
                + RESET)
        if respuesta_4 in ("a", "A"):
            pts /= 2
            func_ans("Oneself", "自", "White")
        elif respuesta_4 in ("b", "B"):
            pts /= 2
            func_ans("Day", "日", "White")
        elif respuesta_4 in ("d", "D"):
            pts /= 2
            func_ans("One Hundred", "百", "White")
        else:
            pts *= 2
            if pts == 0:
                print(CYAN + "\nCorrect!\nBut you still have", pts,
                      "points ಥ⁠‿⁠ಥ" + RESET)
            else:
                print(CYAN + "\nCorrect!\nYou have ", pts,
                      " points now. Congrats!" + RESET)

    elif challenge not in ("Y", "y"):
        print("\nYou got", pts, "points")

    type("\nWant to play again?")
    again = input(
        " Enter Y to play again or any other key to finish the game: ")

    if again not in ("Y", "y"):
        type(BLUE + "\nThanks por playing! See you soon ᕙ⁠( ⁠•⁠ ⁠‿⁠ ⁠•⁠ ⁠)⁠ᕗ" +
             RESET)
        begin_trivia = False
