import math

inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    Answer = 1
    A, B, D = (int(word) for word in inf.readline().split())
    Answer += math.ceil((D - A) / (A - B))

    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()