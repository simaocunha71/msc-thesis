
    sum := 0
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 && lst[i]%2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}

// Time Complexity: O(n)
// Space Complexity: O(1)

// Here's the step-by-step explanation:
// 
// In this problem, we need to find the sum of all the even elements that are at odd indices of the given list.
// 
// We start by initializing a variable sum to 0. This variable will hold the final sum of even elements at odd indices.
// 
// We then use a for loop to iterate over the entire list. For each element in the list, we check if the index (i) is odd (i%2 == 0) and if the element itself is even (lst[i]%2 == 0).
// 
// If both conditions are true, we add the element to the sum variable.
// 
// Finally, we return the sum of all the even elements at odd indices.

// The time complexity of this solution is O(n), where n is the length of the list. This is because we need to iterate over each element in the list once.

// The space complexity of this solution is O(1), indicating constant space. This is because we only use a single variable (sum) to store the result, and its size does not depend on the size of the input.

```
// Given a non-empty list of integers lst. Add the even elements that are at odd indices.
func Add(lst []int) int {
    sum := 0
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 && lst[i]%2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}
```

```python
def add(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            sum += l