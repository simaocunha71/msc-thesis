```
def solution(lst):
    total = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total
```



Explanation:
This function uses a for loop to iterate over the list, starting from the first element and stepping by 2 each time. This ensures that we are only looking at the elements in even positions. For each of these elements, we check if it is odd by using the modulus operator (`%`). If it is odd, we add it to our running total. Finally, we return the total sum of all the odd elements in even positions.