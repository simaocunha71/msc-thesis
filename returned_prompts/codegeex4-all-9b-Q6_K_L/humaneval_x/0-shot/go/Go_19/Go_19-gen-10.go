```go
func SortNumbers(numbers string) string{
    nums := map[string]int{
        "zero":  0,
        "one":   1,
        "two":   2,
        "three": 3,
        "four":  4,
        "five":  5,
        "six":   6,
        "seven": 7,
        "eight": 8,
        "nine":  9,
    }
    numStrings := strings.Split(numbers, " ")
    numValues := make([]int, len(numStrings))
    for i, s := range numStrings {
        numValues[i] = nums[s]
    }
    sort.Ints(numValues)
    sortedNumStrings := make([]string, len(numValues))
    for i, v := range numValues {
        for s, n := range nums {
            if n == v {
                sortedNumStrings[i] = s
                break
            }
        }
    }
    return strings.Join(sortedNumStrings, " ")
}
```