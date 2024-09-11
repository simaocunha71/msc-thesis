```
def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = [0] * n
    for i in range(n):
        cnt[i] = a[i]
        if i > 0:
            cnt[i] += cnt[i-1]

    ans = 0
    for i in range(n):
        for j in range(i,n):
            if i > 0 and a[