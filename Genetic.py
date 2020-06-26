import csv
import math

tsv_file = open("ngrams1.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_fitness(message, gram):
    real_message = "".join(letter for letter in message if letter.isalpha())

    sum = 0.0
    for x in range(0, len(real_message) - gram + 1):
        sum = sum + math.log(get_value(real_message[x: x + gram]), 2)

    return sum


def get_value(word):
    for row in read_tsv:
        if row[0] == word:
            return int(row[1])
    return 1


def encode(message, cipher):
    result = ""

    for x in range(0, len(message)):
        if message[x] not in alpha:
            result += message[x]
        else:
            result += cipher[alpha.find(message[x])]

    return result

def decode(message, cipher):
    result = ""

    for x in range(0, len(message)):
        if message[x] not in alpha:
            result += message[x]
        else:
            result += alpha[cipher.find(message[x])]

    return result


text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
secret = encode(text, "XYZABCDEFGHIJKLMNOPQRSTUVW")
answer = decode(secret, "XYZABCDEFGHIJKLMNOPQRSTUVW")

print(secret)
print(answer)

print(get_fitness(text, 4))
print(get_fitness(secret, 4))

tsv_file.close()

