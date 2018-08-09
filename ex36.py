inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    N, M = (int(word) for word in inf.readline().split())
    house_list = [int(word) for word in inf.readline().split()]
    house_list.sort()
    k = N // 2
    d_sum = 0

    if M == 1:
        k = N // 2
        d_sum = 0
        for i in range(0, N):
            d_sum += abs(int(house_list[i]) - int(house_list[k]))

    '''elif M == 2:
        k = N // 2
        l = k // 2
        d_sum = 0
        for i in range(0, N):
            if i <= k:
                d_sum += abs(int(house_list[i]) - int(house_list[l]))
            else:

                d_sum += abs(int(house_list[i]) - int(house_list[N - (l + 1)]))'''
    Answer = d_sum

    print('Case #%d' % (int(t) + 1))
    print(Answer)
