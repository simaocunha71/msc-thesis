```go
func GetPositive(l []int) []int {
    var positive []int
    for _, v := range l {
        if v > 0 {
            positive = append(positive, v)
        }
    }
    return positive
}
```

Explanation:
The provided function `GetPositive` takes a slice of integers as input and returns a new slice containing only the positive numbers from the original list.

Inside the function, we initialize an empty slice `positive` to store the positive numbers. Then, we iterate over the input slice `l` using a `for` loop with a range variable `v`.

For each iteration, we check if the current value `v` is greater than 0 using the conditional statement `if v > 0`. If the condition is true, we append the positive number to the `positive` slice using the `append` function.

Finally, we return the `positive` slice containing only the positive numbers from the original list. The returned slice is a new, independent copy of the filtered values, rather than a reference to the original slice.

Example usage:
```go
l := []int{-1, 2, -4, 5, 6}
positive := GetPositive(l)
fmt.Println(positive) // [2 5 6]

l = []int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}
positive = GetPositive(l)
fmt.Println(positive) // [5 3 2 3 9 123 1]
```