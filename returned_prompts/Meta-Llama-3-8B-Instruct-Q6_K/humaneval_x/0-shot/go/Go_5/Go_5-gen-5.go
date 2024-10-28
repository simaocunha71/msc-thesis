```go
func Intersperse(numbers []int, delimeter int) []int {
    result := []int{}
    for _, num := range numbers {
        result = append(result, num)
        result = append(result, delimeter)
    }
    return result[:len(result)-1]
}
```
In this solution, we create a new slice `result` and iterate over the input slice `numbers`. For each number, we append it to `result` and then append the `delimeter`. Finally, we return `result` but truncate the last element (which is the `delimeter`) to maintain the original length of the input slice. This approach ensures that the `delimeter` is inserted between each pair of consecutive elements.