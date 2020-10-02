# print("hello")
# userdict = {"set": "hello how are you", "get": "I am fine", "ok": "I am ok"}
# userinput = input("Enter keys")
# print(userdict[userinput])
# print(userdict.get(userinput, "Not Found"))

# Fauly calculator
# while True:
#     num1 = int(input("Enter first number :"))
#     num2 = int(input("Enter second number :"))
#     operation = input("Enter operator :")

#     if num1 == 56 and num2 == 9 and operation == "+":
#         print(77)
#     elif num1 == 45 and num2 == 3 and operation == "*":
#         print(555)
#     elif num1 == 56 and num2 == 6 and operation == "/":
#         print(4)
#     elif operation == "+":
#         print(num1 + num2)
#     elif operation == "*":
#         print(num1 * num2)
#     elif operation == "/":
#         print(num1 / num2)

# myList = [["aditya", 34, 78], ["Rohan", 67, 889], ["carry", 8, 90]]
# for i, k, y in myList:
#     print(i, k, y)

# dict1 = dict(myList)
# print(dict1)

# myList = ["aditya", 78, 4, 2, 56, 43, 79, 0, 2, 5, 1, "hello", [12, 34, 56]]

# for i in myList:
#     if type(i) == int and i > 6:
#         print(i, end=" ")

# n = 18
# no. of guesses 9
# no. of guesses left
# game over

# hiddenNum = 18
# guess = 0

# while guess < 9:
#     inp = input("Guess the number\n")
#     if int(inp) > hiddenNum:
#         guess = guess + 1
#         print(
#             "Input value is greater than the number to be guessed. Please provide lower value.Number of guesses left",
#             (9 - guess),
#         )
#         continue
#     elif int(inp) < hiddenNum:
#         guess = guess + 1
#         print(
#             "Input value is lesser than the number to be guessed.Please provide greater value.Number of guesses left",
#             (9 - guess),
#         )
#         continue
#     elif int(inp) == 18:
#         print("You guessed correct number. You took %d number of guesses" % (guess))
#         break

# Pattern printing

# inp = int(input("Enter Interger number\n"))
# boolvalue = int(input("Enter bool value\n"))
# if boolvalue:
#     for i in range(1, inp + 1):
#         print("*" * i)
# else:
#     for k in range(inp, 0, -1):
#         print("*" * k)

# x = 89


# def func1():
#     x = 20

#     def func2():
#         global x
#         x = 88

#     print("Before calling func2()", x)  # Local scope of func1 20
#     func2()
#     print("After calling func2()", x)  # locak scope of func1 20


# func1()
# print(x)


# l = 56


# def func1():
#     m = 78
#     global l
#     l = 78
#     print(m, l)


# func1()
# print(l)


# def factorial(n):

#     fact = 1
#     for i in range(n):
#         fact = fact * (i + 1)
#     return fact


# number = int(input("Enter any number :"))
# fact = factorial(number)
# print(fact)


# def a_first(a):
#     return a[1]


# a = [[1, 14], [5, 6], [8, 23]]
# a.sort(key=a_first)
# print(a)

# myList = [[12, 34], [45, 31], [56, 89]]
# # print(myList[1])


# def myfunc(a):
#     return a[1]


# myList.sort(key=myfunc)
# # new = myfunc(myList)
# print(myList)

# Random func

# import random
# import math

# a = random.randint(1, 20)
# print(a)
# a = math.floor(random.random() * 20)
# print(a)
# myList = ["mukherjee", "mukesh", "aditya", "girish"]
# newlist = random.choices(myList, 2)
# print(newlist)

# snake water gun game

# Snake water gun

# import random

# lst = ["s", "w", "g"]

# chance = 10
# no_of_chance = 0
# computer_point = 0
# human_point = 0

# print(" \t \t \t \t Snake,Water,Gun Game\n \n")
# print("s for snake \nw for water \ng for gun \n")

# # making the game in while
# while no_of_chance < chance:
#     _input = input("Snake,Water,Gun:")
#     _random = random.choice(lst)

#     if _input == _random:
#         print("Tie Both 0 point to each \n ")

#     # if user enter s
#     elif _input == "s" and _random == "g":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n ")

#     elif _input == "s" and _random == "w":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

#     # if user enter w
#     elif _input == "w" and _random == "s":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n ")

#     elif _input == "w" and _random == "g":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

#     # if user enter g

#     elif _input == "g" and _random == "s":
#         human_point = human_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("Human wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n")

#     elif _input == "g" and _random == "w":
#         computer_point = computer_point + 1
#         print(f"your guess {_input} and computer guess is {_random} \n")
#         print("computer wins 1 point \n")
#         print(f"computer_point is {computer_point} and your point is {human_point} \n ")

#     else:
#         print("you have input wrong \n")

#     no_of_chance = no_of_chance + 1
#     print(f"{chance - no_of_chance} is left out of {chance} \n")

# print("Game over")

# if computer_point == human_point:
#     print("Tie")

# elif computer_point > human_point:
#     print("Computer wins and you loose")

# else:
#     print("you win and computer loose")

# print(f"your point is {human_point} and computer point is {computer_point}")

#
# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
#


# def myfunc(normal, *args, **kwargs):
#     print(type(args))
#     print(normal)
#     for item in args:
#         print(item)
#     print("\nList of key value pair")

#     for key, value in kwargs.items():
#         print(f"{key} is {value}")


# mylist = ["hello", "how", "are", "you"]
# normal = "The tuples are :"
# mydict = {"name": "Gour", "age": 60, "home": "varanasi"}
# myfunc(normal, *mylist, **mydict)
# myfunc(normal, *mylist, name="aditya", age=60, home="varanasi", subject="comsci")

# import time

# mytime = time.asctime(time.localtime(time.time()))
# print(mytime)

# print(time.time())


# Space removing program
# def removespace(input_str):
#     length = len(input_str)
#     i = 0
#     while length:
#         if input_str[i] == " ":
#             continue
#             i = +1
#             length -= 1
#         else:
#             print(input_str)


# input_str = "    Hello    "
# result = removespace(input_str)
# print(result)


# def removespace(inp_str):
#     st = ""
#     for i in inp_str:
#         if i == " ":
#             continue
#         else:
#             st = st + i
#     print(st)


# inp_str = "   hello    "
# new_str = removespace(inp_str)


# def removespace(inp_str):
#     i = 0
#     new_str = ""
#     while i < len(inp_str) - 1:
#         if inp_str[i] == " ":
#             i += 1
#             continue
#         elif inp_str[i] == " " and inp_str[i + 1] is not " ":
#             new_str = new_str + inp_str[i]
#             i += 1
#         else:
#             new_str = new_str + inp_str[i]
#             i += 1
#     print(new_str)


# inp_str = "   hello world  "
# removespace(inp_str)

# secert_num = 9
# guess_count = 0
# tot_count = 3
# while guess_count < tot_count:
#     num = input("Enter number : ")
#     guess_count += 1
#     if int(num) == 9:
#         print("YOU WON ")
#         break
# else:
#     print("Sorry better luck next time")


# Fibonacci series using iterative and recursive approach


# def fiboIterative(n):
#     prevnum = 0
#     currnum = 1
#     for i in range(1, n):
#         prevprev = prevnum
#         prevnum = currnum
#         currnum = prevprev + prevnum
#     return currnum


# def fiboRecursive(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fiboRecursive(n - 2) + fiboRecursive(n - 1)


# if __name__ == "__main__":
#     inp = int(input("Enter the number:\n"))
#     print(f"Value of number using fiboRecursive({inp}) is {fiboRecursive(inp)}")
#     print(f"Value of number using fiboIterative({inp}) is {fiboIterative(inp)}")

# Check for empty list

# emplist = []
# if len(emplist) == 0:
#     print("Empty list")

##Sum of 2 matrices
# def matrix(m, n):
#     o = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             inp = int(input(f"Enter o[{i}][{j}]"))
#             row.append(inp)
#         o.append(row)
#     return o


# def sum_matrix(A, B):
#     output = []
#     for i in range(len(A)):
#         row = []
#         for j in range(len(A[0])):
#             s = A[i][j] + B[i][j]
#             row.append(s)
#         output.append(row)
#     return output


# m = int(input("Enter value of m\n"))
# n = int(input("Enter value of n\n"))

# print("Enter Matrix A")
# A = matrix(m, n)
# print(A)

# print("Enter Matrix B")
# B = matrix(m, n)
# print(B)

# print("Sum of matrix A and B is")
# C = sum_matrix(A, B)
# print(C)

# [[12, 10, 5]
# , [3, 2, 6],
# [2, 8, 10]]

# [[12, 10, 5], [3, 2, 6], [2, 8, 10]]

# Kirana shop calculator
sum = 0

while True:
    userInp = input("Enter the price item or press q to quit\n")
    if userInp != "q":
        sum = sum + int(userInp)
        print(f"Your bill so far {sum}")
    else:
        print(f"Thank you for shopping with us. Your bill total is {sum}")
        break
