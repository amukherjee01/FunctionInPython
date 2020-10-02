
def func1():
    x = 20

    def func2():
        global x
        x = 88

    print("Before calling func2()", x)  # Local scope of func1 20
    func2()
    print("After calling func2()", x)  # locak scope of func1 20


func1()
print(x)


# l = 56


def func1():
    m = 78
    global l
    l = 78
    print(m, l)


func1()
print(l)


def factorial(n):

    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact


number = int(input("Enter any number :"))
fact = factorial(number)
print(fact)


inp_str = "   hello    "
new_str = removespace(inp_str)


def removespace(inp_str):
    i = 0
    new_str = ""
    while i < len(inp_str) - 1:
        if inp_str[i] == " ":
            i += 1
            continue
        elif inp_str[i] == " " and inp_str[i + 1] is not " ":
            new_str = new_str + inp_str[i]
            i += 1
        else:
            new_str = new_str + inp_str[i]
            i += 1
    print(new_str)


inp_str = "   hello world  "
removespace(inp_str)


# Fibonacci series using iterative and recursive approach


def fiboIterative(n):
    prevnum = 0
    currnum = 1
    for i in range(1, n):
        prevprev = prevnum
        prevnum = currnum
        currnum = prevprev + prevnum
    return currnum


def fiboRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRecursive(n - 2) + fiboRecursive(n - 1)


if __name__ == "__main__":
    inp = int(input("Enter the number:\n"))
    print(f"Value of number using fiboRecursive({inp}) is {fiboRecursive(inp)}")
    print(f"Value of number using fiboIterative({inp}) is {fiboIterative(inp)}")

Check for empty list

emplist = []
if len(emplist) == 0:
    print("Empty list")

#Sum of 2 matrices
def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter o[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o


def sum_matrix(A, B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            s = A[i][j] + B[i][j]
            row.append(s)
        output.append(row)
    return output


m = int(input("Enter value of m\n"))
n = int(input("Enter value of n\n"))

print("Enter Matrix A")
A = matrix(m, n)
print(A)

print("Enter Matrix B")
B = matrix(m, n)
print(B)

print("Sum of matrix A and B is")
C = sum_matrix(A, B)
print(C)

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
