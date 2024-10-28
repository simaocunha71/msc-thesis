```go
func Add(lst []int) int {
    var sum int
    for i := 0; i < len(lst); i++ {
        if i%2 != 0 && lst[i]%2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}
```

Explanation:

*   The function `Add` takes a slice of integers `lst` as input.
*   It initializes a variable `sum` to 0, which will store the sum of even elements at odd indices.
*   It iterates over the slice using a for loop, with the variable `i` representing the index.
*   Inside the loop, it checks two conditions:
    *   `i%2 != 0`: This ensures that the index `i` is odd (i.e., 1, 3, 5, ...).
    *   `lst[i]%2 == 0`: This ensures that the element at index `i` is even.
*   If both conditions are true, it adds the element at index `i` to the `sum`.
*   Finally, the function returns the `sum`.