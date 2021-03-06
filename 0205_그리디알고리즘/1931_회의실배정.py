# 끝나는 시간이 빠른 회의를 선택한다.

n = int(input())
conference = []
for _ in range(n):
    start, end = map(int, input().split())
    conference.append((start, end))

# 끝나는 시간으로 오름차순 정렬한다.
# 끝나는 시간이 같은 경우, 시작시간으로 오름차순 정렬한다.
conference = sorted(conference, key=lambda c: (c[1], c[0]))

# 시작시간 >= 이전 회의의 끝나는 시간일 경우 회의실 배정 가능.
## 회의는 중단되지 않는다.
## 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
start_now = conference[0][0]
end_now = conference[0][1]
cnt = 1
for start_next, end_next in conference[1:]:
    if end_now > start_next:
        continue
    start_now, end_now = start_next, end_next
    cnt += 1

print(cnt)
