```
def find_sum(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    sum = 0
    for num, count in count_dict.items():
        if count == 1:
            sum += num
    return sum
```


Explanation: 
This function works by first creating a dictionary where the keys are the numbers in the list and the values are the counts of each number. Then it iterates over the dictionary and adds the numbers that have a count of 1 (i.e., the non-repeated elements) to the sum. The sum of these non-repeated elements is then returned. 

The unit test `assert find_sum([1,2,3,1,1,4,5,6]) == 21` helps to clarify the problem by providing an example of a list and the expected result. This test can be used to verify that the function is working correctly. 





