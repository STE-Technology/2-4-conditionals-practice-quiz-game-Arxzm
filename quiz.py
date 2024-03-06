"""
File: quiz.py
Author: arsham
Date: 2024-03-05
Description: multiple choice game that calculates score
"""
print("mutiple question quiz game (FIFA)")

correct_answers = 0

print("1. who scored the most goals in the worldcup?")
print("(a) Messi")
print("(b) Ronaldo")
print("(c) Neymar")

answer_1 = input("Answer:")

if answer_1 == "a" or answer_1 == "A":
    print("correct!")
    correct_answers += 1
else:
    print ("incorrect")

print("2. which team won the world cup in 2014?")
print("(a) France")
print("(b) germany")
print("(c) portugal")

answer_2 = input("Answer:")

if answer_2 == "b" or answer_2 == "B":
    print("correct!")
    correct_answers += 1
else:
    print ("incorrect")   

print("3. which team had the post points in 2018?")
print("(a) barcelona")
print("(b) real madrid")
print("(c) bayern munich")

answer_3 = input("Answer:")

if answer_3 == "c" or answer_3 == "c":
        print("correct!")
        correct_answers += 1
else:
        print ("incorrect")

# calculates the percentage score
score_percentage = (correct_answers / 3) * 100

# print the quiz complrtion message with the score
print(f"Quiz complete! you answred {correct_answers} out of 3, your score is {score_percentage} %")





