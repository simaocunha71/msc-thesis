```go
func Add(lst []int) int {
    var sum int
    for i, v := range lst {
        if i%2 != 0 && v % 2 == 0 {
            sum += v
        }
    }
    return sum
}
```



The function `Add` takes a slice of integers `lst` as input and returns the sum of the even elements that are at odd indices. It initializes a variable `sum` to zero and iterates over the slice using a range loop. For each element `v` at index `i`, it checks if `i` is odd (using the modulus operator `%`) and if `v` is even (using the modulus operator `%`). If both conditions are true, it adds `v` to `sum`. Finally, it returns the value of `sum`.

For example, if the input is `[4, 2, 6, 7]`, the function will iterate over the slice and add `2` (at index 1) and `6` (at index 2) to `sum`, resulting in a final sum of `2 + 6 = 8`. If the input is `[1, 3, 5, 7]`, the function will not add any elements to `sum` because there are no even elements at odd indices. If the input is `[2, 4, 6, 8]`, the function will add all elements to `sum` because all elements are even and at odd indices.