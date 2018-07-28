import sys
import math

inf = open('input.txt')
T = inf.readline()

for t in range(0, int(T)):
    input_num = inf.readline()
    input_num = int(input_num)
    Answer: int = 0

    if input_num < 4:
        Answer = 2
        print('Case #%d' % (int(t) + 1))
        print(Answer)
        continue

    sqr_input = int(math.sqrt(input_num))
    Answer = input_num + 1

    # n = 2 일 때
    for i in range(sqr_input, 0, -1):
        if(input_num % i == 0) & (i < (input_num / i) - 1) & (Answer > (input_num / i) - 1):
            Answer = input_num // i - 1
            break

    # n > 2 일 때
    i: int = 2
    while (i < Answer) & (i <= sqr_input):
        sum_element: int = 1
        mul_element = i
        while sum_element < input_num:
            sum_element += mul_element
            mul_element *= i
            if (input_num % sum_element == 0) & ((input_num / sum_element) < i):
                Answer = i
                break
        i += 1

    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()