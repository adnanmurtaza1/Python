import csv
import math
import random
from random import randint


POPULATION_SIZE = 500
CLONES = 1
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN = .75
CROSSOVER_POINTS = 5
MUTATION_RATE = .8
NGRAM = 3
MESSAGE = """W CTZV VYQXDVD MCWJ IVJJTHV, TYD VYQXDVD WM BVAA, FXK WM QXYMTWYJ MCV JVQKVM XF MCV PYWZVKJV! YX
KVTAAS, WM DXVJ! SXP DXY&#39;M NVAWVZV IV? BCS BXPAD SXP YXM NVAWVZV MCTM MCWJ RVKFVQMAS QKXIPAVYM JVQKVM
MVGM QXYMTWYJ MCV NV TAA, VYD TAA, HKTYDVJM JVQKVM XF TAA MCV QXJIXJ? YXB W FVVA DWJKVJRVQMVD! CTZV
SXP DWJQXZVKVD SXPK XBY NVMMVK PAMWITMV MKPMC XF VZVKSMCWYH? W DWDY&#39;M MCWYL JX. JX BCS TKV SXP HVMMWYH
TAA PRRWMS TM IV? CXYVJMAS. YX XYV CTJ TYS ITYYVKJ MCVJV DTSJ. ...BCTM&#39;J MCTM? SXP BTYM IV MX MVAA
SXP MCV JVQKVM? YXM TFMVK MCWJ LWYD XF DWJKVJRVQM! HXXDYVJJ HKTQWXPJ IV. NTQL BCVY W BTJ T SXPMC W
BTJ YXM JX QTAAXPJ. BCVY JXIVXYV BVAA KVJRVQMVD TYD WIRXKMTYM MXAD IV MCTM MCVS CTD JXIVMCWYH BXKMC
MVAAWYH IV, W OPJM AWJMVYVD! W DWDY&#39;M DXPNM MCVI! JX KPDV, CXYVJMAS. OPJM PYTQQVRMTNAV."""


tsv_file = open("ngrams1.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic = {}
for row in read_tsv:
    if len(row[0]) == NGRAM:
        dic[row[0]] = int(row[1])

population = []
x = 0
while x < POPULATION_SIZE:
    temp_cipher =''.join(random.sample(alpha, len(alpha)))
    if temp_cipher not in population:
        population.append(temp_cipher)
        x = x + 1



def get_fitness(message, gram):
    real_message = "".join(letter for letter in message if letter.isalpha())

    sum = 0.0
    for x in range(0, len(real_message) - gram + 1):
        sum = sum + math.log(get_value(real_message[x: x + gram]), 2)

    return sum

def get_value(word):
    if word in dic:
        return dic.get(word)

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

def mutate(cipher):
    index = randint(0, 25)
    index2 = randint(0, 25)
    while index2 == index:
        index2 = randint(0, 25)

    if index < index2:
        return cipher[0: index] + cipher[index2] + cipher[index + 1: index2] + cipher[index] + cipher[index2 + 1:]

    return cipher[0: index2] + cipher[index] + cipher[index2 + 1: index] + cipher[index2] + cipher[index + 1:]

def breed(parent1, parent2):
    child= []
    for x in range(26):
        child.append("temp")

    arr = []
    crossed = 0
    while crossed != CROSSOVER_POINTS:
        loc = randint(0, 25)
        arr.append(loc)
        if child[loc] == "temp":
            crossed = crossed + 1
            child[loc] = parent1[loc]

    index_child = 0
    for x in range(0, 26):
        while index_child < 25 and child[index_child] != "temp":
            index_child = index_child + 1

        if parent2[x] not in child:
            child[index_child] = parent2[x]
            index_child = index_child + 1

    result = ""
    for y in range(26):
        result = result + child[y]

    return result

def select_parents(population):
    tourney1 = random.sample(population, TOURNAMENT_SIZE)
    tourney2 = random.sample(population, TOURNAMENT_SIZE)

    tourney1 = sorted(tourney1, key=lambda cipher: get_fitness(decode(MESSAGE, cipher), NGRAM))
    tourney2 = sorted(tourney2, key=lambda cipher: get_fitness(decode(MESSAGE, cipher), NGRAM))

    max = TOURNAMENT_SIZE - 1
    while random.random() > TOURNAMENT_WIN:
        max = max - 1
    if max < 0:
        max = 0

    max2 = TOURNAMENT_SIZE - 1
    while random.random() > TOURNAMENT_WIN:
        max2 = max2 - 1
    if max2 < 0:
        max2 = 0

    return tourney1[max], tourney2[max2]

generation = 1
while True: # start the actual process now
    best = max(population, key=lambda cipher: get_fitness(decode(MESSAGE, cipher), NGRAM))
    print("Generation " + str(generation) + ": " + decode(MESSAGE, best) + " " + str(get_fitness(decode(MESSAGE, best), NGRAM)))

    temp_population = []
    x = 0
    while x < TOURNAMENT_SIZE:
        dad, mom = select_parents(population)
        child = breed(dad, mom)
        if random.random() <= MUTATION_RATE:
            child = mutate(child)
        if child not in temp_population:
            temp_population.append(child)
            x = x + 1

    population = temp_population
    generation = generation + 1









tsv_file.close()

