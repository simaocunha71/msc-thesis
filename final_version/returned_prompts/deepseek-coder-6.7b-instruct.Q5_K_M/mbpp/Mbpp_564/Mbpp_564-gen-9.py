
def count_Pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_Pairs([1,2,1])) # 2

Explanation:
The function works by iterating through the list and for each element, it checks all the elements after it to ensure it isn't the same. If the elements are different, it increments the count by one. This approach ensures that each pair is counted only once.


