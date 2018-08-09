inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    N = int(inf.readline())
    S_list = [0 for _ in range(0, N)]  # 속도
    L_list = [0 for _ in range(0, N)]  # 길이
    D_list = [0 for _ in range(0, N)]  # 시작점
    f_time = 0  # 결승선 통과하는 시간
    f_line = 0
    for i in range(0, N):
        info_list = [int(word) for word in inf.readline().split()]
        S_list[i] = info_list[0]
        L_list[i] = info_list[1]
        D_list[i] = info_list[2]

    while True:
        ok_list = [False for _ in range(0, N)]
        for i in range(0, N):
            f_line = (S_list[i] * f_time + D_list[i]) % L_list[i]
            if f_line == 0:
                ok_list[i] = True
        if ok_list.count(True) == N:
            break
        else:
            f_time += 1

    Answer = f_time

    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()