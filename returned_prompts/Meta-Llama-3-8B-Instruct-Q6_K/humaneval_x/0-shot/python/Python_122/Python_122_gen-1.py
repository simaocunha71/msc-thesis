    def add_elements(arr, k):
        sum = 0
        for i in range(k):
            if len(str(arr[i])) <= 2:
                sum += arr[i]
        return sum

# Test the function
print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # Output: 24
print(add_elements([1,2,3,4,5,6,7,8,9], 9)) # Output: 24
print(add_elements([1000000,1,2,3,4,5,6,7,8,9], 9)) # Output: 45
print(add_elements([111,111,111,111,111,111,111,111,111,111], 10)) # Output: 0
print(add_elements([1,2,3,4,5,6,7,8,9,10], 10)) # Output: 35
print(add_elements([100,1000,10000,100000,1000000], 5)) # Output: 1110
print(add_elements([1,2,3,4,5,6,7,8,9,10], 10)) # Output: 55
print(add_elements([111,111,111,111,111,111,111,111,111,111], 10)) # Output: 0
print(add_elements([111,111,111,111,111,111,111,111,111,111], 9)) # Output: 0
print(add_elements([111,111,111,111,111,111,111,111,111,111], 8)) # Output: 0
print(add_elements([111,111,111,111,111,111,111,111,111,111], 7)) # Output: 0
print(add_elements([111,111,111,111,111,111,111,111,111,111], 6)) # Output: 0
print(add_elements([111,111,111,111,111,111,111,111,111,111], 5)) # Output: 0
print(add_elements([111,111,111,111,111,111,111,111,111,111], 4)) # Output: 0
print(add_elements([111,111,