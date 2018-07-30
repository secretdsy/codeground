import math
import sys

inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    scores = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]
    A, B, C, D, E = (int(word) for word in inf.readline().split())
    user_score = 0
    N = inf.readline()

    for i in range(0, int(N)):
        x, y = (int(word) for word in inf.readline().split())
        d = math.sqrt(x ** 2 + y ** 2)

        if d > E: # out board
            continue
        elif d < A: # bull
            user_score += 50
            continue

        theta = math.atan2(y, x)
        theta *= (180 / math.pi)
        theta += 9
        theta = (theta + 360) % 360
        num = int(theta / 18)
        score = scores[num]

        if d > D and d < E:  # double
            user_score += score * 2
        elif d < C and d > B:  # triple
            user_score += score * 3
        else:  # single
            user_score += score

    Answer = user_score
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()
