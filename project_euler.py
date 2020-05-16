''' Problem 1
sum = 0
for x in range(1, 1000):
    if x % 3 == 0 or x % 5 ==0:
        print(x)
        sum += x

print(sum)
'''







''' PROBLEM 2
list = [1, 1, 2];

num = 2;
while num < 4000000 :
    list.append(list[len(list) - 1] + list[len(list) - 2])
    num = list[len(list) - 1]

sum = 0;
for x in range(1, len(list) - 1):
    if list[x] % 2 == 0 :
        sum += list[x]

print(sum)
'''








''''' PROBLEM 3
def isPrime(num):
    for x in range(2, num):
        if(num % x == 0):
            return False
    return True


list = []
num = 600851475143
x=2
while(isPrime(num) == False):
    while True:
        if isPrime(x) and num % x == 0:
            list.append(x)
            num = int(num/x)
            x = 2
            break
        else:
            x += 1
list.append(num)

print (max(list))
print (list)
'''''









''''#  PROBLEM 4
def isPallindrome(num):

    # temp = str(int(num))
    # list1 = []
    # list2 = []
    # for x in range(0, len(temp)):
    #     list1.append(temp[x])
    # for x in reversed(range(0, len(temp))):
    #     list2.append(temp[x])
    # for y in range(0, len(temp)):
    #     if list1[y] != list2[y]:
    #         return False
    # return True

    temp = str(int(num))
    tempr = temp[len(temp) : : -1]
    if temp == tempr:
        return True
    return False

max = 0
maxf = 0
maxl = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        if isPallindrome(x*y) and x*y > max:
            max = x*y
            maxf = x
            maxl = y

print(str(maxf) + "x" + str(maxl) + "=" + str(max))
'''







""" PROBLEM 8
name = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''

list1 = name.split("\n")
fstr = "";
for element in list1:
    fstr = fstr + element

def Product(str):
    pro = 1;
    for x in range(0, len(str)):
        pro = pro * int(str[x])
    return pro

max = 0
for x in range(0, len(fstr) - 13):
    temp = Product(fstr[x : x + 13])
    if temp > max:
        max = temp

print(max)
"""






""" PROBLEM 9
def findA(b):
    a = (1000000 - 2000*b)/(2000 - 2*b) #equation to find a if b is given
    if(a - int(a) == 0): #checks if its a natural number
        return a
    return -1

b = 0;
for x in range(1, 500):
    if(findA(x) != -1):
        a = findA(x)
        b = x
        c = 1000 - b - a

print(str(int(a)) + "^2 + " + str(int(b)) + "^2 = " + str(int(c)) + "^2")
print("product is " + str(int(a*b*c)))
"""
