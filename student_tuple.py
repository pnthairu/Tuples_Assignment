# Start Program
"""
Program: student_tuple.py
Author: Paul Thairu
Last date modified: 06/019/2020

In this assignment you will tie together the seemingly unrelated tuple and
arbitrary argument list to perform file input and output.

Write a function write_to_file() that accepts a tuple to be added to the end of a file
"""

def write_to_file(student):
    file = open("open_student_information.txt", "a")  # Opening text file
    file.write(str(student) + '\n')  # write content to the text file as string
    file.close()  # closing text file


def get_student_info(name):
    print("NOTE: To enter next student score type '-1' on the 'Enter the test score' ")
    print("Please enter test score for student", name)
    test_scores = []  # declaring a list
    while True:
        scores = input("Enter the test scores: ")
        if scores == "-1": # if score is -1 go to the next student and enter the score
            break
        test_scores.append(float(scores))
    student = (name, test_scores)  # making a list of student name and the score
    write_to_file(student)


def read_from_file():
    file = open("open_student_information.txt", 'r')
    lines = file.readlines()  # read all lines at a go
    for line in lines:
        print(line)  # printing each line which has student name and score


if __name__ == '__main__':
    open("open_student_information.txt", 'w').close()
    names = ["Paul", "Beth", "Soe", "Bessy", "Alex"]  # hard coding list of student names
    for i in range(0, len(names)):
        get_student_info(names[i])  # function call get_student_info and assigning names
    read_from_file()  # function call read line

# End program
