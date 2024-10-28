
def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst = list(set(lst))
    lst.sort()
    return lst[1] if len(lst) > 1 else None


print(next_smallest([1, 2, 3, 4, 5])) # 2
print(next_smallest([5, 1, 4, 3, 2])) # 2
print(next_smallest([])) # None
print(next_smallest([1, 1])) # None


# 다른 사람의 풀이

def next_smallest(lst):
    return sorted(set(lst))[1] if len(set(lst)) > 1 else None

def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1] if lst[0] != lst[1] else (lst[2] if len(lst) > 2 else None)

def next_smallest(lst):
    return min(x for x in lst if x > min(lst)) if len(set(lst)) > 1 else None

def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst = list(dict.fromkeys(lst))
    lst.sort()
    return lst[1]

print(next_smallest([1, 2, 3, 4, 5])) # 2
print(next_smallest([5, 1, 4, 3, 2])) # 2
print(next_smallest([])) # None
print(next_smallest([1, 1])) # None

# 모두 같은 결과를 반환합니다. 주어진 목록의