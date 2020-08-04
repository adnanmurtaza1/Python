import numpy as np

def step(num):
    if num > 0:
        return 1
    return 0

def apply_function(A, arr):
    for x in range(arr.size):
        arr[x] = A(arr[x])
    return arr

def sigmoid(num):
    return 1/(1+ np.exp(0 - num))

def circle_function1(num):
    if num > 1:
        return 0
    return 1

def circle_function2(num):
    if num > 1:
        return 0
    return 1

'''
#XOR HAPPENS HERE
input = np.array([1, 0])

#LAYER 1
w_layer1 = np.array([[-1, -2], [1, 1]])
w_layer1 = w_layer1.transpose()
result_1 = np.matmul(input, w_layer1)
b_layer1 = np.array([3, 0])
result_1 = apply_function(step, result_1 + b_layer1)

#LAYER 2 (OUTPUT)
w_layer2 = np.array([1, 2])
w_layer2 = w_layer2.transpose()
result_2 = np.matmul(result_1, w_layer2)
b_layer2 = np.array([-2])
result_2 = apply_function(step, result_2 + b_layer2)

print(result_2)
'''


'''
#DIAMOND HAPPENS HERE
input = np.array([0.234, -0.546])

#LAYER 1
w_layer1 = np.array([[-1, 1], [-1, 1], [1, 1], [1, 1]])
w_layer1 = w_layer1.transpose()
result_1 = np.matmul(input, w_layer1)
b_layer1 = np.array([1, -1, -1, 1])
result_1 = apply_function(step, result_1 + b_layer1)

#LAYER 2 (OUTPUT)
w_layer2 = np.array([1, -1, -1, 2])
w_layer2 = w_layer2.transpose()
result_2 = np.matmul(result_1, w_layer2)
b_layer2 = np.array([-2])
result_2 = apply_function(step, result_2 + b_layer2)

print(result_2)
'''
#'''
w_layer1 = np.array([[-1, 1], [-1, 1], [1, 1], [1, 1]])
w_layer1 = w_layer1.transpose()
og_bias = np.array([1, -1, -1, 1])
b_layer1 = np.array([1, -1, -1, 1], dtype=float)
frac = 0.66

for x in range(500):
    input = np.random.uniform(-1, 1, 2)
    actual = circle_function1((input[0]**2 + input[1]**2)**0.5)

    result = sigmoid(w_layer1[0][0] * input[0] + input[1] * w_layer1[1][0] + b_layer1[0])
    if result != actual:
        b_layer1[0] = b_layer1[0] + (result - actual)*frac

    result = sigmoid(w_layer1[0][1]  * input[0] + input[1] * w_layer1[1][1] + b_layer1[1])
    if result != actual:
        b_layer1[1] = b_layer1[1] + (result - actual)*frac

    result = sigmoid(w_layer1[0][2] * input[0] + input[1] * w_layer1[1][2] + b_layer1[2])
    if result != actual:
        b_layer1[2] = b_layer1[2] + (result - actual)*frac

    result = sigmoid(w_layer1[0][3] * input[0] + input[1] * w_layer1[1][3] + b_layer1[3])
    if result != actual:
        b_layer1[3] = b_layer1[3] + (result - actual)*frac

old_work = 0
new_work = 0
for x in range(500):
    input = np.random.uniform(-1, 1, 2)
    actual = circle_function1((input[0]**2 + input[1]**2)**0.5)
    # LAYER 1
    result_1 = np.matmul(input, w_layer1)
    result_1 = apply_function(sigmoid, result_1 + og_bias)
    trained_result = apply_function(sigmoid, result_1 + b_layer1)

    # LAYER 2 (OUTPUT)
    w_layer2 = np.array([1, -1, -1, 2])
    w_layer2 = w_layer2.transpose()
    result_2 = np.matmul(result_1, w_layer2)
    trained_2 = np.matmul(trained_result, w_layer2)
    b_layer2 = np.array([-2])
    result_2 = apply_function(step, result_2 + b_layer2)
    trained_2 = apply_function(step, trained_2 + b_layer2)
    if result_2[0] == 1:
        old_work += 1
    if trained_2[0] == 1:
        new_work += 1

print(old_work)
print(new_work)
print(b_layer1)
#'''

