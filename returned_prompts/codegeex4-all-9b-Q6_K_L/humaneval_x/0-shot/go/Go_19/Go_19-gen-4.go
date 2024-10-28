```go
func SortNumbers(numbers string) string {
    split := strings.Fields(numbers)
    numMap := map[string]int{
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    sort.Slice(split, func(i, j int) bool {
        return numMap[split[i]] < numMap[split[j]]
    })
    return strings.Join(split, " ")
}
```