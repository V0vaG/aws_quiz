import json
import os
import time

json_file = "qa.json"

def showOptionAnswer(question_dict, isFiftyFifty):
    print("\n {questionNo}) {question}".format(questionNo=i + 1, question=question_dict['q']))
    if i > 0:
        score = (rightAnswer/i)*100
    else:
        score = 0
    optionBuilder = ""
    for key, value in sorted(question_dict.items()):
        if key == 'ca' or key == 'q':
            continue
        optionBuilder += key + "/"
        print(" <{optionNo}> {option}".format(optionNo=key, option=value))

    print("\nScore: ", score, "(", rightAnswer, "/", i, ")")
    answer = input("Enter the option (1/2/3/4) or 0 to quit: ")
    return answer

def play():
    with open(json_file, "r", encoding='utf-8') as qa:
        questionSet = qa.read()
        questionsList = json.loads(questionSet)
        print(len(questionsList), "Questions.")
        global rightAnswer
        rightAnswer = 0
        global i
        i = 0
        while i < len(questionsList):
            question_dict = questionsList[i]
            answer = showOptionAnswer(question_dict, False)
            i += 1

            if answer == '0':
                print("\nGame Over")
                exit()

            if question_dict['ca'] == answer:
                print("RIGHT answer :-)")
                rightAnswer += 1
                time.sleep(1)
                os.system("clear")
            else:
                print("\nWRONG Answer :-(")
                print("\nThe Correct answer is {correctAnswer}".format(correctAnswer=question_dict['ca']))
                time.sleep(3)
                os.system("clear")
        else:
            print("Game Over!\n")
    play()

def edit():
    def make_json(que, ans1, ans2, ans3, ans4, c_ans):
        os.system("sh json_fix.sh")
        dict1 = {"q": que, "1": ans1, "2": ans2, "3": ans3, "4": ans4, "ca": c_ans}
        out_file = open(json_file, "a")
        json.dump(dict1, out_file, indent=4)
        out_file.close()
        os.system("sh json_fix2.sh")

    def input_question():
        os.system("clear")
        que = input("Enter Question: ")
        if que == '0':
            exit()
        ans1 = input("Enter #1 answer: ")
        if ans1 == '0':
            exit()
        ans2 = input("Enter #2 answer: ")
        if ans2 == '0':
            exit()
        ans3 = input("Enter #3 answer: ")
        if ans3 == '0':
            exit()
        ans4 = input("Enter #4 answer: ")
        if ans4 == '0':
            exit()
        c_ans = input("Enter Correct answer num: ")
        if c_ans == '0':
            exit()
        make_json(que, ans1, ans2, ans3, ans4, c_ans)
        input_question()

    input_question()

print(" ~~~~~~ WELCOME TO QUIZ APP ~~~~~")
ansx = input("Enter p-play, e-edit: ")
if ansx == 'p':
    time.sleep(1)
    os.system("clear")
    play()
elif ansx == 'e':
    edit()
    time.sleep(1)
    os.system("clear")
else:
    exit()

