inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    N = int(inf.readline())
    tree_list = [int(word) for word in inf.readline().split()]
    laser_list = [int(word) for word in inf.readline().split()]
    total = 0
    cut = 0
    min_laser = laser_list[0]

    for i in range(1, N):
        min_laser = min(min_laser, laser_list[i] - i)

    for i in range(0, N):
        cut = tree_list[i] - min_laser
        if cut > 0:
            total += cut

    Answer = total
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()
