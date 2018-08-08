inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    N = int(inf.readline())
    P_list = [int(word) for word in inf.readline().split()]
    Q_list = [int(word) for word in inf.readline().split()]
    dp = [0 for _ in range(0, N)]

    dp[0] = max(P_list[0], Q_list[0])
    dp[1] = max(dp[0] + P_list[1], Q_list[1])

    for i in range(2, N):
        dp[i] = max(dp[i - 2] + Q_list[i], dp[i - 1] + P_list[i])
    Answer = dp[N - 1]
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()
