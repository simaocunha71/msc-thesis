The problem requires finding the minimum number of changes needed to make an array palindromic. A palindromic array reads the same forwards and backwards. 

For example, the array [1, 2, 3, 5, 4, 7, 9, 6] is not palindromic, but after changing 4 elements, it becomes [1, 2, 3, 3, 2, 1], which is palindromic.

The solution involves comparing the first element of the array with the last, the second with the second last, and so on. If they are not the same, it counts as one change. The process continues until the middle of the array is reached. 

Here is a possible implementation in Go:

```go
func SmallestChange(arr []int) int {
    changes := 0
    n := len(arr)
    for i := 0; i < n/2; i++ {
        if arr[i] != arr[n-1-i] {
            changes++
        }
    }
    return changes
}
```

This function takes an array of integers as input and returns the minimum number of changes needed to make it palindromic. The function iterates over the first half of the array and compares each element with its corresponding element from the end of the array. If they are not the same, it increments the `changes` counter. Finally, it returns the total number of changes.

The time complexity of this solution is O(n), where n is the length of the array. This is because the function iterates over the array once, comparing each element with its corresponding element from the end of the array.

The space complexity of this solution is O(1) because it only uses a constant amount of extra space to store the `changes` counter.