inf = open('input.txt')

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    hello = inf.readline()
    cnt_h = hello.count('h')
    cnt_e = hello.count('e')
    cnt_l = hello.count('l') // 2
    cnt_o = hello.count('o')
    if cnt_h > 0 and cnt_e > 0 and cnt_l > 0 and cnt_o > 0:
        Answer = min(cnt_h, cnt_e, cnt_l, cnt_o)

    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()
