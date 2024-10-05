
def exchange(lst1, lst2):
    odd_lst1 = []
    odd_lst2 = []
    for i in lst1:
        if i % 2 != 0:
            odd_lst1.append(i)
    for i in lst2:
        if i % 2 != 0:
            odd_lst2.append(i)
    if odd_lst2 == []:
        return "NO"
    else:
        for i in odd_lst1:
            if odd_lst2.count(i):
                odd_lst2.remove(i)
        if odd_lst2 == []:
            return "YES"
        else:
            return "NO"


def exchange2(lst1, lst2):
    lst1 = [i for i in lst1 if i%2 == 1]
    lst2 = [i for i in lst2 if i%2 == 1]
    if len(lst1) == 0:
        return "YES"
    else:
        return "NO"

def exchange3(lst1, lst2):
    odd_lst1 = [i for i in lst1 if i%2 == 1]
    odd_lst2 = [i for i in lst2 if i%2 == 1]
    odd_lst2.extend(odd_lst1)
    odd_lst2.sort()
    odd_lst1.sort()
    if odd_lst2 == odd_lst1:
        return "YES"
    else:
        return "NO"



# Please enter the values of lst1 and lst2, separated by a space
lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
print(exchange3(lst1, lst2))
































```