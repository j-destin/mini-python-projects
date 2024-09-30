import sys
import os
import time
from questions import questions 


def clear():
    os.system('cls')    
    
def seperate():
    print('----------------------------------------')

def quiz():
    clear()
    print('''
                                ------------------------------
                                NOTE: ENTER Q TO QUIT
                                ------------------------------
          ''')
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question['options']:
            print(option)
        userAnswer = input("ANSWER:: ").upper()
        if userAnswer == question["answer"]:
            print(f'<<< RESULT : Correct >>>!!')
            seperate()
            score+=1
        elif userAnswer == 'Q':
            sys.exit()
        else:
            print(f'<<< RESULT : Oh Damm You lose LOSER, The correct answer is {question["answer"]} >>>')
    print(f"""
___________________________________________________________________________________
          SCORE : <<< You got {score} questions out of {len(question)+1} right >>>
-----------------------------------------------------------------------------------
          """)
    time.sleep(5)
    clear()
    
while True:
    quiz()