def solution(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 1)

print(solution([5, 8, 7, 1])) 
print(solution([3, 3, 3, 3, 3])) 
print(solution([30, 13, 24, 321]))