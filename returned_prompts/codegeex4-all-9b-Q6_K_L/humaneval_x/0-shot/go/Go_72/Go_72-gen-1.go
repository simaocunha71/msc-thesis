You can use the following code to solve the problem:

```go
func WillItFly(q []int,w int) bool {
    // Check if the slice is a palindrome
    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-1-i] {
            return false
        }
    }
    // Check if the sum of the slice elements is less than or equal to the maximum possible weight
    if sum(q) <= w {
        return true
    }
    return false
}

// Helper function to calculate the sum of a slice
func sum(q []int) int {
    total := 0
    for _, num := range q {
        total += num
    }
    return total
}
```

Explanation:
1. The function `WillItFly` takes a slice `q` and an integer `w` as input and returns a boolean value.
2. The first step is to check if the slice `q` is a palindrome. This is done by comparing the elements from the start and end of the slice. If any pair of elements is not equal, the function returns `false`.
3. If the slice `q` is a palindrome, the next step is to check if the sum of its elements is less than or equal to the maximum possible weight `w`. This is done by calling the helper function `sum` to calculate the sum of the slice elements and comparing it to `w`.
4. If the sum is less than or equal to `w`, the function returns `true`, otherwise it returns `false`.
5. The helper function `sum` takes a slice `q` as input and returns the sum of its elements. It initializes a variable `total` to 0 and iterates over the slice, adding each element to `total`. Finally, it returns the total sum.