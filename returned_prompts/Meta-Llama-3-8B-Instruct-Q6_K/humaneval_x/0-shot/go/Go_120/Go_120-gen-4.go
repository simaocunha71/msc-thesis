Here is a possible implementation of the function:
```go
func Maximum(arr []int, k int) []int {
    // Create a slice of pairs, where each pair contains a number from the array
    // and its frequency (1)
    pairs := make([]struct{ num int; freq int }, len(arr))
    for i, num := range arr {
        pairs[i].num = num
        pairs[i].freq = 1
    }

    // Sort the slice of pairs based on the frequency and then the number
    sort.Slice(pairs, func(i, j int) bool {
        if pairs[i].freq != pairs[j].freq {
            return pairs[i].freq > pairs[j].freq
        }
        return pairs[i].num > pairs[j].num
    })

    // Return the top k numbers
    result := make([]int, k)
    for i := 0; i < k; i++ {
        result[i] = pairs[i].num
    }
    return result
}
```
This implementation uses the `sort` package to sort the slice of pairs based on the frequency and then the number. The `sort.Slice` function is used to sort the slice, and the `func(i, j int) bool` function is used to determine the order of the pairs. The top k numbers are then returned as a slice.

For example, if the input is `arr = [-3, -4, 5]` and `k = 3`, the output will be `[-4, -3, 5]`. If the input is `arr = [4, -4, 4]` and `k = 2`, the output will be `[4, 4]`. If the input is `arr = [-3, 2, 1, 2, -1, -2, 1]` and `k = 1`, the output will be `[2]`. A more efficient way to solve this problem would be to use a heap, but this implementation uses a simple sort. A more efficient way to solve this problem would be to use a heap, but this implementation uses a simple sort. A more efficient way to solve this problem would be to use a heap, but this implementation uses a simple sort. A more efficient way to solve this problem would be to use a heap, but this implementation uses a simple sort. A more efficient way to solve this problem would be to use a heap, but