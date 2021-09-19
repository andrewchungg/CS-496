# 1

def factorial(N):
    if N < 0:
        return 0  # factorial DNE for neg numbers
    elif N == 0:
        return 1  # 0! = 1
    else:
        factorial = 1
        for i in range(1, N + 1):  # loop for product of successive terms
            factorial = factorial * i
        return factorial


# 2

def oddProduct(integers):
    for i in range(0, len(integers)):  # loop and test to see if there are odd products
        for j in range(i + 1, len(integers)):
            if ((integers[i] * integers[j] % 2 != 0 and integers[i] != integers[j])):
                return True
    return False  # if no odd product return false


integers = [1, 3, 4]
print(oddProduct(integers))


# 3

def reverse(number):
    answer = int(str(number)[::-1]) if number >= 0 else -int(
        str(-number)[::-1])  # convert number to string and check if > 0
    return answer if -2 ** 31 <= answer <= 2 ** 31 - 1 else 0  # return answer if between max allowable bounds


# 4

def removeCommas(sentence):
    finalStr = ""
    for character in sentence:
        if character != ",":  # if character is not a comma, add to finalStr
            finalStr = finalStr + character
    return finalStr


# 5

def checkBrackets(string):
    brackets = []
    for char in string:
        if char in ['[', '{', '(']:  # if char is opening bracket add to list
            brackets.append(char)
        if len(brackets) == 0:  # if list is empty
            return False
        if char == ']' and brackets.pop() != '[':
            return False
        if char == '}' and brackets.pop() != '{':
            return False
        if char == ')' and brackets.pop() != '(':
            return False
    if len(brackets) == 0:
        return True
    else:
        return True


# 6

def mergeLists(list1, list2):
    output = []     # output list
    i = 0       # list 1 index
    j = 0       # list 2 index

    while i < len(list1) and j < len(list2):        # loop until both lists have elements
        if list1[i] < list2[j]:     # if element in list1 is smaller
            output.append(list1[i])     # add to output list
            i += 1
        else:                       # if element in list2 is smaller
            output.append(list2[j])     # add to output list
            j += 1
    output = output + list1[i:] + list2[j:]
    return output
