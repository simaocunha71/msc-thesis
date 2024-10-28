You can use a map to keep track of the frequency of each number, and then iterate over the original list to add only the numbers with frequency 1 to the result. Here's how you can do it in Go:

```go
func RemoveDuplicates(numbers []int) []int {
    frequency := make(map[int]int)
    for _, num := range numbers {
        frequency[num]++
    }
    result := []int{}
    for _, num := range numbers {
        if frequency[num] == 1 {
            result = append(result, num)
        }
    }
    return result
}
```

This code first creates a map called `frequency` to keep track of the frequency of each number in the input list. Then, it iterates over the original list and adds only the numbers with frequency 1 to the result list. Finally, it returns the result list.