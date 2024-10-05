def solution(lst):
    return sum([i for i in lst[1::2] if i%2==1])

print(solution([5, 8, 7, 1])) #==> 12
print(solution([3, 3, 3, 3, 3])) #==> 9
print(solution([30, 13, 24, 321])) #==>0