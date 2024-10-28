You can use a two-pointer approach to solve this problem. Start with two pointers, one at the beginning of the array and the other at the end. If the elements at these two pointers are equal, move both pointers towards the center. If they are not equal, change the element at the pointer with the larger value to be equal to the element at the other pointer, and then move both pointers towards the center. Repeat this process until the two pointers meet or cross each other. The number of changes made during this process will be the minimum number of elements that need to be changed to make the array palindromic.

Here is the implementation in Go:

```go
func SmallestChange(arr []int) int {
    left := 0
    right := len(arr) - 1
    changes := 0

    for left < right {
        if arr[left] != arr[right] {
            changes++
        }
        left++
        right--
    }

    return changes
}
```

The time complexity of this solution is O(n), where n is the length of the array.