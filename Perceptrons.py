import ast

def step(num):
    if num > 0:
        return 1
    return 0

def truth_table(bits, n):
    size = 2**bits
    answers = fix_conversion(size, n)
    result = ()
    current = size - 1
    while current > -1:
        result = result + ((fix_conversion(bits, current), answers[size - current - 1]), )
        current = current - 1

    return result

def fix_conversion(bit, num):
    tup = ()
    tup = dec_to_binary(num, tup)
    while len(tup) < bit:
        tup = (0,) + tup
    return tup

def dec_to_binary(num, tup):
    if num > 1:
       tup = dec_to_binary(num//2, tup)

    tup = tup + (num%2, )
    return tup

def pretty_print_tt(table):
    if len(table) != 0:
        for x in range(0, len(table)):
            for y in range(0, len(table[0][0])):
                print(table[x][0][y], " ", end="")
            print("|", table[x][1], end= "")
            print()

def perceptron(A, w, b, x):
    return A(dot_product(w, x) + b)

def dot_product(vec1, vec2):
    sum = 0
    for x in range(0, len(vec1)):
        sum = sum + vec1[x]*vec2[x]

    return sum

def check(n, w, b):
    temp_table = truth_table(len(w), n)
    denominator = float(len(temp_table))
    numerator = 0.0
    for x in range(len(temp_table)):
        if perceptron(step, w, b, temp_table[x][0]) == temp_table[x][1]:
            numerator = numerator + 1

    return float(numerator/denominator)


n = 9
w = (1, 1)
bit = len(w)
b = -1.5
pretty_print_tt(truth_table(bit, n))
print(check(n, w, b))

