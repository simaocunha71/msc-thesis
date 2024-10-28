Here's the solution you were looking for:

```go
func IncrList(l []int) []int {
    for i := range l {
        l[i]++
    }
    return l
}
```

This function takes a slice of integers (`l`) as an argument and increments each element in the slice by 1. It then returns the modified slice.

The `for i := range l` loop iterates over each index in the slice `l`. Inside the loop, `l[i]++` increments the value at index `i` by 1.

The `return l` statement returns the modified slice `l` after the loop has finished incrementing each element.

You can test the function with the following code:

```go
func main() {
    l := []int{1, 2, 3}
    fmt.Println(IncrList(l)) // Output: [2 3 4]
    
    l = []int{5, 3, 5, 2, 3, 3, 9, 0, 123}
    fmt.Println(IncrList(l)) // Output: [6 4 6 3 4 4 10 1 124]
}
```

This code creates a slice `l` with the values `[1, 2, 3]` and calls the `IncrList` function on it. The modified slice is then printed to the console.

Similarly, it creates a new slice `l` with the values `[5, 3, 5, 2, 3, 3, 9, 0, 123]` and calls the `IncrList` function on it again. The modified slice is then printed to the console.