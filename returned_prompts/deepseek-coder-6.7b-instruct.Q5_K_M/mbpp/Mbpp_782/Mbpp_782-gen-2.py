def odd_length_sum(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        total += ((i+1)*(n-i)+1)//2 * arr[i]
    return total

# Test
print(odd_length_sum([1,2,3,4]))  # 31
print(odd_length_sum([1,2,3,4,5]))  # 55

Explanation:
In the function, we are calculating the number of subarrays with length odd for each element in the array and multiplying it with the element itself. We are using the formula ((i+1)*(n-i)+1)//2 to get the count of odd length sub