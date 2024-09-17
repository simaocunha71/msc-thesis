```
def count_Pairs(lst, k):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j] and lst[i] < k and lst[j] < k:
                count += 1
    return count
```    
The function `count_Pairs` takes a list of integers `lst` and an integer `k` as inputs. It iterates over the list with two nested loops to generate all possible unordered pairs. For each pair, it checks if both elements are unequal and less than `k`. If the condition is met, it increments the `count` variable. Finally, it returns the `count` which represents the number of possible unordered pairs where both elements are unequal. The unit test `assert count_Pairs([1,2,1],3) == 2` helps to clarify the problem by providing a specific input and expected output.  



