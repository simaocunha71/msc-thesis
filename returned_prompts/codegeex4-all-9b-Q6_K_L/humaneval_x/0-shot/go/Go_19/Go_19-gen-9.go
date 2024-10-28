```go
func SortNumbers(numbers string) string {
    numMap := map[string]int{
        "zero": 0,
        "one":  1,
        "two":  2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six":  6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    numList := strings.Fields(numbers)
    sort.Slice(numList, func(i, j int) bool {
        return numMap[numList[i]] < numMap[numList[j]]
    })
    return strings.Join(numList, " ")
}
```