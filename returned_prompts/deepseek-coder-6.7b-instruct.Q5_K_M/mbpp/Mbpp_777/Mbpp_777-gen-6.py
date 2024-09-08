
def find_sum(lst):
    s = set()
    for i in lst:
        if i not in s:
            s.add(i)
    return sum(s)

print(find_sum([1,2,3,1,1,4,5,6])) # 21


