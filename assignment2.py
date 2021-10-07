# Question 3

# non recursive #1
def findMax1(a):
    minval = a[0]
    maxval = a[0]
    for i in range(len(a)):
        if a[i]>maxval:
            maxval = a[i]
        if a[i] < minval:
            minval = a[i]
    print("max = ", maxval, ", min = ", minval)


# non recursive #2
def findMax2(a):
    minval = a[0]
    maxval = a[0]
    for val in a:
        if val>maxval:
            maxval = val
        if val<minval:
            minval = val
    print("max = ", maxval, ", min = ", minval)


# Question 4

def findMinRec(a, n):
   if (n==1):
        return a[0]
   return min(a[n-1], findMinRec(a, n-1))

def findMaxRec(a, n):
    if (n==1):
        return a[0]
    return max(a[n-1], findMaxRec(a, n-1))

def reverseString(s):
    if len(s) == 0:
        return
    temp = s[0]
    reverseString(s[1:])
    print(temp, end='')


# Driver

if __name__ == '__main__':
    a = [10, 39, 47, 1, 49, 100]
    n = len(a)
    findMax1(a)
    findMax2(a)
    print("Max num is ", findMaxRec(a, n))
    print("Min num is ", findMinRec(a, n))
    s = "SDSU@San"
    reverseString(s)