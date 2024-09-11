"""
def interleave_lists(list1, list2, list3):
    return [x for i in range(len(list1)) for x in [list1[i], list2[i], list3[i]]]
"""

def interleave_lists(list1, list2, list3):
    return list(itertools.chain(list1, list2, list3))


def interleave_lists(list1, list2, list3):
    return list(zip(list1, list2, list3))

def interleave_lists(list1, list2, list3):
    return sum([list1, list2, list3],[])

def interleave_lists(list1, list2, list3):
    return [*list1,*list2,*list3]

def interleave_lists(list1, list2, list3):
    return list(zip(*[iter(list1),iter(list2),iter(list3)]))


def interleave_lists(list1, list2, list3):
    return [*zip(list1, list2, list3)]


# Python3 program to interleave
# given three lists
def interleave_lists(list1, list2, list3):
    l = list(zip(list1, list2, list3))
    # converting tuple to list
    for i in range(len(l)):
        l[i] = list(l[i])
    return l


# Driver program
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = [10, 20, 30, 40, 50, 60, 70]
    list3 = [100, 200, 300, 400, 500, 600, 700]
    print(interleave_lists(list1, list2, list3))


def interleave_lists(list1, list2, list3):
    return [*list1,*list2,*list3]
