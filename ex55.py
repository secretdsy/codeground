import sys

inf = open('input.txt')
#inf = sys.stdin


def tower(n, beg, aux, end):
    if n == 1:
        print(beg, "->", end)
    else:
        tower(n-1, beg, end, aux)
        tower(1, beg, aux, end)
        tower(n-1, aux, beg, end)


T = inf.readline()

for t in range(0, int(T)):
    N = int(inf.readline())
    print('Case #%d' % (int(t) + 1))
    tower(N, 1, 2, 3)
inf.close()

# http://woongheelee.com/entry/%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%80%EC%9B%8C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98