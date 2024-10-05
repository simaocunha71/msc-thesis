```go
func Intersperse(numbers []int, delimeter int) []int {
    var result []int
    for _, num := range numbers {
        result = append(result, num)
        result = append(result, delimeter)
    }
    return result[:len(result)-1]
}
```

Explanation:

*   We create an empty slice `result` to store the interspersed elements.
*   We iterate over the input slice `numbers` using a range loop.
*   For each number, we append it to the `result` slice and then append the `delimeter` to the `result` slice.
*   After the loop, we return the `result` slice, but we slice it to exclude the last `delimeter` element that was appended.
*   This ensures that the `delimeter` is only inserted between consecutive elements, not after the last element.