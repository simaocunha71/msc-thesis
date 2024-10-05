The provided solution is an incorrect implementation of the problem. It does not correctly add the even elements that are at odd indices. Let's break down the problem and correct the solution:

1. **Understand the Problem**: We need to add the values of even numbers that are located at odd indices in the given list.
2. **Identify Steps to Solve**: 
    - Iterate through the list.
    - Check if the current index is odd (i.e., index+1 is even).
    - Check if the value at the current index is even.
    - If both conditions are met, add the value to a sum.

Here is the corrected implementation:

```go
func Add(lst []int) int {
    sum := 0
    for i := 0; i < len(lst); i++ {
        if (i+1)%2 == 0 && lst[i]%2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}
```

Let's explain this code step by step:

1. We initialize a variable `sum` to store the sum of the even elements at odd indices.
2. We loop through the list using a `for` loop.
3. Inside the loop, we check if the index `(i+1)` is even, which means the current index is odd. We do this by checking if `(i+1) % 2 == 0`.
4. We also check if the element at the current index is even by checking if `lst[i] % 2 == 0`.
5. If both conditions are true, we add the element to `sum`.
6. After the loop, we return the `sum`.

This corrected solution should now correctly calculate the sum of even elements at odd indices in the given list.