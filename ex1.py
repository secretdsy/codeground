import sys

inf = sys.stdin

T = inf.readline();

for t in range(0, int(T)):

    Answer = 0

    num = inf.readline()
    num_list = inf.readline()
    num_list = num_list.split()

    Answer = int(num_list[0])
    for n in range(0, int(num) - 1):
        Answer = Answer ^ int(num_list[n + 1])

    print('Case #%d' % (int(t) + 1))
    print(Answer)
