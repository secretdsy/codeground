import sys

inf = open('input.txt')
#inf = sys.stdin

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    num_list = []
    N = inf.readline()

    for i in range(0, int(N)):
        app_num = int(inf.readline())
        num_list.append(app_num)

    num_list.sort()
    print(num_list)
    num_sum: int = 0

    for i in range(0, int(N)):
        if i % 2 == 0:
            num_sum += num_list[i]
        elif i % 2 == 1:
            num_sum -= num_list[i]

    Answer = num_sum
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()