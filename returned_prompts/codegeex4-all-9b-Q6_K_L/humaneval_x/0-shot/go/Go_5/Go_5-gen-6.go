```go
func Intersperse(numbers []int, delimeter int) []int {
    if len(numbers) < 2 {
        return numbers
    }
    result := make([]int, 0, len(numbers)*2-1)
    for i, num := range numbers {
        result = append(result, num)
        if i != len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}
```
The function `Intersperse` takes a slice of integers `numbers` and an integer `delimeter` as input and returns a new slice with the `delimeter` inserted between every two consecutive elements of `numbers`. If the length of `numbers` is less than 2, it returns `numbers` as is. Otherwise, it creates a new slice `result` with a length of `len(numbers)*2-1` to accommodate the `delimeter` and `numbers`. It then iterates over the elements of `numbers`, appending each element to `result` and the `delimeter` if it is not the last element of `numbers`. Finally, it returns `result`.