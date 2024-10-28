from functools import reduce
from itertools import izip
def count_same_pair(list_1,list_2):
    count=0
    for i in range(len(list_1)):
        if list_1[i]==list_2[i]:
            count+=1
    return count