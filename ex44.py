inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    Answer = 1

    N = int(inf.readline())
    label = [False for _ in range(N + 1)]
    M = int(inf.readline())
    in_a = [0 for _ in range(M)]
    in_b = [0 for _ in range(M)]

    for i in range(0, M):
        x, y = (int(word) for word in inf.readline().split())
        in_a[i] = x
        in_b[i] = y
        label[in_b[i]] = not(label[in_a[i]])

    for i in range(0, M):
        if label[in_a[i]] == label[in_b[i]]:
            Answer = 0
            break

    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()
