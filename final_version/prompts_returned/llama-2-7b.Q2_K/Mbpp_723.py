"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""

def same(a, b):
    if a == [1 for _ in range(len(b))]:
        return (True, len(list(filter(lambda x: x in a, set(range())))))
    elif b == [1 for _ in range(len(a))]:
        return (True, len(list(filter(lambda x: x in b, set(range())))), )
    else:
        return False

def count_same_pair(lsts):
    def check_same(a, b):
        ans, same = same(a, b)
        if not same:
            print("a", a,"\n", "b", b,"\n", same)
        return ans
    
    sames = 0
    for lst in lsts:
        for num in list(filter(lambda x: x in lst, set(range()))):
            if num not in lst:
                break
            ssame = check_same([num], lst)
            ssame and (ssame[1]+=1); continue
            
    return sum([x for (a,b),x in zip_star(*lsts)])==len(lsts[0])
    
if __name__ == '__main__':
    print "Test case 1"
    count_same_pair([1,2], [1, 3])
    print
    print "Test case 2"
    count_same_pair(
        [[1, 2, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9]],
        [[6, 7, 8, 9],[2, 2, 3, 1, 2, 6]]
    )
