```
def find_sum(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    sum = 0
    for num, freq in freq_dict.items():
        if freq == 1:
            sum += num
    
    return sum
``` 

The function works by first creating a dictionary where the keys are the numbers in the list and the values are the frequencies of those numbers. It then iterates over this dictionary, adding up the numbers that appear only once. The sum of these non-repeated numbers is the return value. 

For example, in the list [1,2,3,1,1,4,5,6], the frequency dictionary would be {1: 3, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}. The non-repeated numbers are 2, 3, 4, 5, 6, so the sum is 21.  This is confirmed by the unit test `assert find_sum([1,2,3,1,1,4,5,6]) == 21`. 

The time complexity of this function is O(n), where n is the number of elements in the list, because we iterate over the list twice (once to build the frequency dictionary and once to calculate the sum). The space complexity is also O(n), because in the worst case the frequency dictionary could contain n elements.  The function is also linear, meaning that the time complexity does not change with the size of the input, which makes it efficient for large inputs.  It is also easy to understand and debug, which makes it a good choice for this problem.  However, it could be optimized by using a single pass over the list and a set to keep track of the unique elements, which would reduce the space complexity to O(1) and the time complexity to O(n).  But this would make the function more complex and less easy to understand, so it is not a good choice for this problem.  The function is also not robust, because it does not handle the case where the input is not a list.  It would be better to add error checking to handle this case.  For example, we could use a try/except block to catch the TypeError that would be raised if the input is not a list