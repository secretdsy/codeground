import sys
inf = open('input.txt')

#inf = sys.stdin

T = inf.readline()

for t in range(0, int(T)):
    Answer = 1
    N = inf.readline()  # 총 스톤 개수
    stone_list = inf.readline()  # 스톤 리스트
    stone_list = stone_list.split()
    for i in range(0, int(N)):
        stone_list[i] = int(stone_list[i])
    max_stone = int(inf.readline())  # 최대 이동 가능 거리
    now: int = 0
    '''
    Traceback (most recent call last): File line 15, in max_stone = int(inf.readline()) # 최대 이동 가능 거리ValueError: invalid literal for int() with base 10: '392561 761935 815178 1401098 2357177 2610620 3480170 4944679 7049848 7376145 7772966 8591354 9294083 10592712 11019275 12408998 12930557 13011796 14044292 14082923 15563367 16817320 17688091 19722938
    '''

    for i in range(0, int(N)):
        max_next = now + max_stone
        if stone_list[i] < max_next:  # 최대 갈 수 있는 거리보다 작을 때
            continue
        elif stone_list[i] == max_next:  # 최대 갈 수 있는 거리랑 같을 때
            now = stone_list[i]
            Answer += 1
        else:  # 최대 갈 수 있는 거리보다 클 때
            if (stone_list[0] > max_next) | (now == stone_list[i - 1]):
                Answer = -1
                break
            else:
                now = stone_list[i - 1]
                Answer += 1
                i -= 1

    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()