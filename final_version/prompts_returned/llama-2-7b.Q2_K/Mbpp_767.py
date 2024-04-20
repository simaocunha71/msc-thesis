"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""
def get_pairs(list, sum):
    count = 0
    if len(set(list)) != len(list):
        count += 1
    #for element in list:
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if set([i,j]) & {sum}:
                print("pairs found")
                break
            else:
                pass

def get_pairs_count(list, sum):
    return get_pairs([i for i in list], sum)
