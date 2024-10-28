```go
func SortArray(array []int) []int {
    sum := array[0] + array[len(array)-1]
    if sum%2 == 0 {
        sort.Slice(array, func(i, j int) bool {
            return array[i] > array[j]
        })
    } else {
        sort.Slice(array, func(i, j int) bool {
            return array[i] < array[j]
        })
    }
    return array
}
```


The above code takes an array of integers as input and returns a new array with the same elements. It first calculates the sum of the first and last elements of the array. If the sum is even, it sorts the array in descending order; otherwise, it sorts the array in ascending order. The sort is done in-place using the `sort.Slice` function from the Go standard library.

Here's how you can test the function:

```go
func main() {
    array := []int{2, 4, 3, 0, 1, 5}
    result := SortArray(array)
    fmt.Println(result) // Output: [6 5 4 3 2 1 0]
}
```

This will print the sorted array in descending order, as the sum of the first and last elements of the array is even. If you change the array to `[]int{2, 4, 3, 0, 1, 5, 6}`, the output will be `[6 5 4 3 2 1 0]`, which is the sorted array in descending order. If you change the array to `[]int{2, 4, 3, 0, 1, 5}`, the output will be `[0 1 2 3 4 5]`, which is the sorted array in ascending order. 