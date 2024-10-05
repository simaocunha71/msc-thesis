```
def by_length(arr):
    num_names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    result = []
    
    for num in arr:
        if 1 <= num <= 9:
            result.append(num_names[num])
        else:
            result.append(num_names.get(num, 'Invalid number'))  # if num is not in 1-9 range, return 'Invalid number'
    
    result = result[::-1]
    
    return result
```


Explanation:
*   We create a dictionary `num_names` that maps each number from 1 to 9 to its corresponding name.
*   We iterate over each number in the input array `arr`. If the number is between 1 and 9, we append its corresponding name to the result list. If the number is not in this range, we append 'Invalid number' to the result list.
*   We reverse the result list using slicing (`result[::-1]`).
*   Finally, we return the result list. If the input array is empty, the function returns an empty list. If the array contains any numbers outside the range 1-9, the function will return 'Invalid number' for those numbers.