import sys

inf = open('input.txt')
#inf = sys.stdin

T = inf.readline();

for t in range(0, int(T)):

    Answer = 0

    sub_num = inf.readline()
    sub_num = sub_num.split()
    score_list = inf.readline()
    score_list = score_list.split()
    for i in range(len(score_list)):
        score_list[i] = int(score_list[i])
    score_list.sort()  # 반환 값을 변수에 저장하면 NoneType 됨
    score_list.reverse()
    print(score_list)
    for n in range(0, int(sub_num[1])):
        Answer += int(score_list[n])
        print(Answer)
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()