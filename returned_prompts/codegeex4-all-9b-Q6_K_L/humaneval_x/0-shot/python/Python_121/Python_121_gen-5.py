def solution(lst):
    return sum(i for j, i in enumerate(lst) if j % 2 == 0 and i % 2 != 0)