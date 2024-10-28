```go
func SortNumbers(numbers string) string {
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
    nums := strings.Fields(numbers)
    sort.Slice(nums, func(i, j int) bool {
        return numMap[nums[i]] < numMap[nums[j]]
    })
    return strings.Join(nums, " ")
}
```