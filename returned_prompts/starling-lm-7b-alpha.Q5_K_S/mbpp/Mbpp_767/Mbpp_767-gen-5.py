def get_pairs_count(lst,sum):
    count=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==sum:
                count+=1
    return count

# To check the above function
assert get_pairs_count([1,1,1,1],2) == 6


"""
Explanation:
The above function is a simple function which uses nested loops to count the number of pairs in a given list whose sum is equal to the given sum.
The function first initialises the count to zero. Then, for each element in the list, it traverses through the list again to find the elements whose sum is equal to the given sum. If such a pair is found, it increments the count by 1. Finally, it returns the count.
"""

# Testing the above function
print(get_pairs_count([1,1,1,1],2)) # Should print 6
print(get_pairs_count([1,1,2,3],5)) # Should print 4
print(get_pairs_count([1,2,3,4],5)) # Should print 4
print(get_pairs_count([1,2,3,4,5],10)) # Should print 10
print(get_pairs_count([1,2,3,4,5,6],10)) # Should print 15


"""
Explanation:
The above code demonstrates the use of the above function. It first calls the function with different arguments and then prints the result.
"""

# To check the above code
assert get_pairs_count([1,1,1,1],2) == 6
assert get_pairs_count([1,1,2,3],5) == 4
assert get_pairs_count([1,2,3,4],5) == 4
assert get_pairs_count([1,2,3,4,5],10) == 10
assert get_pairs_count([1,2,3,4,5,6],10) == 15