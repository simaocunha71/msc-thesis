```go
func UniqueDigits(x []int) []int {
    var y []int
    for _, v := range x {
        if !hasEvenDigit(v) {
            y = append(y, v)
        }
    }
    sort.Slice(y, func(i, j int) bool {
        return y[i] < y[j]
    })
    return y
}

func hasEvenDigit(n int) bool {
    for n > 0 {
        if n%2 == 0 {
            return true
        }
        n /= 10
    }
    return false
}
```

The function `UniqueDigits` iterates through the input slice `x` and checks if each number does not have an even digit using the helper function `hasEvenDigit`. If a number does not have an even digit, it is appended to the output slice `y`.

After iterating through all the numbers, the output slice `y` is sorted in increasing order using the `sort.Slice` function. Finally, the sorted slice `y` is returned.

The helper function `hasEvenDigit` checks if a given number `n` has an even digit. It does this by repeatedly dividing the number by 10 and checking the remainder when divided by 2. If the remainder is 0, it means the number has an even digit and the function returns true. If the number becomes 0 without finding an even digit, the function returns false.