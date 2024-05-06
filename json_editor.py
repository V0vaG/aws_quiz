import json
import os

def make_json(que, ans1, ans2, ans3, ans4, c_ans):
    os.system("sh json_fix.sh")
    dict1 = {"q": que, "1": ans1, "2": ans2, "3": ans3, "4": ans4, "ca": c_ans}
    out_file = open("qa.json", "a")
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
