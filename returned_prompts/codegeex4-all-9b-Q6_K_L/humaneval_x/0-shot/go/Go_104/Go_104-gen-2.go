```go
func UniqueDigits(x []int) []int {
    var result []int
    for _, num := range x {
        hasEven := false
        for _, digit := range strconv.Itoa(num) {
            if digit%2 == 0 {
                hasEven = true
                break
            }
        }
        if !hasEven {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}
```

Explanation:
1. We create an empty slice `result` to store the numbers without even digits.
2. We iterate through each number in the input slice `x`.
3. For each number, we convert it to a string and iterate through each digit.
4. If we find any digit that is even, we set `hasEven` to `true` and break out of the loop.
5. If we did not find any even digit in the current number, we append it to the `result` slice.
6. After iterating through all the numbers, we sort the `result` slice in increasing order using `sort.Ints`.
7. Finally, we return the `result` slice.