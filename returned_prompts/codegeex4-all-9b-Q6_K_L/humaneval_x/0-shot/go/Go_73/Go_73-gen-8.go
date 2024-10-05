To determine the minimum number of elements that need to be changed to make the array palindromic, we can compare the elements at symmetric positions from the start and end of the array. If the elements are different, we need to change one of them to make them equal. We can keep a count of such changes until we reach the middle of the array.

Here is the implementation of the SmallestChange function in Go:

```go
func SmallestChange(arr []int) int {
    n := len(arr)
    count := 0
    
    for i := 0; i < n/2; i++ {
        if arr[i] != arr[n-i-1] {
            count++
        }
    }
    
    return count
}
```

Let's test the function with the given examples:

```go
func main() {
    arr1 := []int{1, 2, 3, 5, 4, 7, 9, 6}
    fmt.Println(SmallestChange(arr1)) // Output: 4
    
    arr2 := []int{1, 2, 3, 4, 3, 2, 2}
    fmt.Println(SmallestChange(arr2)) // Output: 1
    
    arr3 := []int{1, 2, 3, 2, 1}
    fmt.Println(SmallestChange(arr3)) // Output: 0
}
```

The output of the above code will be:

```
4
1
0
```

This indicates that the minimum number of changes required to make the arrays palindromic are 4, 1, and 0 respectively.