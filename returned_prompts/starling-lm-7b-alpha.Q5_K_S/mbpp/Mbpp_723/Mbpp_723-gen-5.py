def count_same_pair(list_1,list_2):
    count=0
    for i in range(len(list_1)):
        if list_1[i]==list_2[i]:
            count+=1
    return count


# Another method is to use zip function to zip the two lists
# Then use list comprehension to check if the zipped values are equal.
def count_same_pair_alt(list_1,list_2):
    return len([x for x in zip(list_1,list_2) if x == (x[0],x[1])])



# Testing the two methods
print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])) # 4
print(count_same_pair_alt([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])) # 4



# Another method using reduce function
from functools import reduce

def count_same_pair_alt_reduce(list_1,list_2):
    return reduce(lambda x,y:x+y,[1 if x[0]==x[1] else 0 for x in zip(list_1,list_2)])

# Testing the reduce method
print(count_same_pair_alt_reduce([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])) # 4




# Another method using itertools.izip function
from itertools import izip

def count_same_pair_alt_izip(list_1,list_2):
    return len([x for x in izip(list_1,list_2) if x == (x[0],x[1])])

# Testing the izip method
print(