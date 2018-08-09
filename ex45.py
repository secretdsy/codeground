import sys

inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    N, M = (int(word) for word in inf.readline().split())
    test_list = []
    Answer = 0
    for i in range(0, N):
        test_list.append(int(inf.readline()))
    test_list.sort()
    test_list.reverse()
    k: int = 0
    tmp = M

    for i in range(0, N):
        for j in range(i, N):
            tmp -= test_list[j]
            k += test_list[j]
            if tmp < 0:
                tmp += test_list[j]
                k -= test_list[j]
        Answer = max(k, Answer)

    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()
