
def most_frequent(lst):
    counts = {num: lst.count(num) for num in lst}
    max_count = max(counts.values())
    max_nums = [num for num, count in counts.items() if count == max_count]
    return min(max_nums)

print(most_frequent([1,2,3,3,2,2,2,1,1,1]))

# Given the list [1,2,3,3,2,2,2,1,1,1], the most frequent integer is 1 and 2,