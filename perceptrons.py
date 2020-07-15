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

def sum_vectors(vec1, vec2):
    sum = ()
    for index in range(len(vec1)):
        sum = sum + (vec1[index] + vec2[index],)

    return sum

def scalar_vector(scale, vec):
    result = ()
    for index in range(len(vec)):
        result = result + (scale*vec[index], )

    return result
'''
n = 9
w = (1, 1)
bit = len(w)
b = -1.5
pretty_print_tt(truth_table(bit, n))
print(check(n, w, b))
'''




def table_work(bit, num, og_og_weight, og_og_bias, change_frac):
    table = truth_table(bit, num)
    og_weight= og_og_weight
    og_bias = og_og_bias
    for epoch in range(0, 100): #running all the epochs for a single table
            temp_weight = og_weight
            temp_bias = og_bias
            for row in range(len(table)):
                vector_x = table[row][0]
                table_answer = table[row][1]
                p_value = perceptron(step, og_weight, og_bias, vector_x)
                if p_value != table_answer:
                    og_weight = sum_vectors(og_weight, scalar_vector(((table_answer - p_value)*change_frac), vector_x))
                    og_bias = og_bias + (table_answer - p_value)*change_frac

            if (temp_weight == og_weight and temp_bias == og_bias) or epoch == 100:
                works = True
                for row in range(len(table)):
                    vector_x = table[row][0]
                    table_answer = table[row][1]
                    p_value = perceptron(step, og_weight, og_bias, vector_x)
                    if p_value != table_answer:
                        works = False
                if works == True:
                    pretty_print_tt(table)
                    print(og_weight, og_bias)
                    return works
                    break #breaks out of the epoch loop
    return False



'''
og_og_weight = (0, 0)
bit = len(og_og_weight)
og_og_bias = 0
change_frac = 1
working = 0


for table_num in range(2**(2**bit)):
    if table_work(bit, table_num, og_og_weight, og_og_bias, change_frac):
        working = working + 1

print(str(working) + " of the possible " + str(2**(2**bit)) + " tables work")
'''

print(table_work(2, 8, (0, 0), 0, 1))