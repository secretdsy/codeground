inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    Answer = "Y"
    N, M, K = (int(word) for word in inf.readline().split())
    type_list = [0 for _ in range(M + 1)]
    price_list = [0 for _ in range(M + 1)]
    k = 0
    sum_price = 0

    for i in range(0, N):
        k = int(inf.readline())
        type_list[k] += 1
        print("type_list", type_list)
    for i in range(1, M + 1):
        price_list[i] = int(inf.readline())
        print("price_list", price_list)
    for i in range(1, M + 1):
        sum_price += type_list[i] * price_list[i]
        print("sum_price", sum_price)
        if sum_price > K:
            Answer = "N"
            break

    print('Case #%d' % (int(t) + 1))
    print(Answer)
