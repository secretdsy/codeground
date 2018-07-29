import sys

inf = open('input.txt')
#inf = sys.stdin

T = inf.readline()

for t in range(0, int(T)):

    Answer = 0

    N = int(inf.readline())
    scores = []

    for i in range(N):
        scores.append(int(inf.readline()))

    scores = sorted(scores)
    win_score = max(map(lambda x, y: x + N - y, scores, range(N)))

    cnt = len(list(filter(lambda x: x + N >= win_score, scores)))
    Answer = cnt

    print('Case #%d' % (int(t) + 1))
    print(Answer)

inf.close()


'''def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid + 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


def binary_search_not_match(target, data):
    start = 0
    end = len(data) - 1
    mid: int = 0

    while start <= end:
        mid = (start + end) // 2

        if data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    if data[mid] > target:
        return mid
    else:
        mid += 1
        return mid


inf = open('input.txt')
#inf = sys.stdin

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    N = int(inf.readline())
    case_list = [0 for _ in range(N)]
    added_list = [0 for _ in range(N)]
    case_sum: int = 0

    for i in range(0, N):
        in_num = int(inf.readline())
        case_list[i] = in_num
        case_sum += case_list[i]

    if case_sum / len(case_list) == case_list[0] / 1:
        Answer = N
        print('Case #%d' % (int(t) + 1))
        print(Answer)
        continue

    case_list.sort()

    for i in range(0, N):
        added_list[i] = case_list[i] + N - i

    added_list.sort()

    max_num = added_list[N - 1]

    tar = max_num - N

    if binary_search(tar, case_list):
        Answer = N - binary_search(tar, case_list) + 1
    else:
        Answer = N - binary_search_not_match(tar, case_list)

    print('Case #%d' % (int(t) + 1))
    print(Answer)

inf.close()'''