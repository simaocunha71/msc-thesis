```go
func UniqueDigits(x []int) []int {
    unique := make([]int, 0)
    for _, num := range x {
        if !hasEvenDigit(num) {
            unique = append(unique, num)
        }
    }
    sort.Ints(unique)
    return unique
}

func hasEvenDigit(num int) bool {
    for num > 0 {
        digit := num % 10
        if digit%2 == 0 {
            return true
        }
        num /= 10
    }
    return false
}
```

Explanation:
1. We define a function `UniqueDigits` that takes a slice of integers `x` as input and returns a sorted slice of integers.
2. We create an empty slice `unique` to store the numbers without even digits.
3. We iterate over each number in the input slice `x` using a for loop.
4. For each number, we call the helper function `hasEvenDigit` to check if it contains any even digit.
5. If `hasEvenDigit` returns `false`, we append the number to the `unique` slice.
6. After iterating over all numbers, we sort the `unique` slice in increasing order using the `sort.Ints` function.
7. Finally, we return the sorted `unique` slice.