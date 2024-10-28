To solve this problem, we can use a two-pointer approach. We'll start with two pointers, one at the beginning of the array and the other at the end. We'll compare the elements at these two pointers. If they are equal, we move both pointers towards the center. If they are not equal, we increment the count and move the pointer that points to the element that is smaller towards the center. This way, we can find the minimum number of elements that need to be changed to make the array palindromic.

Here is the solution in Go:

```go
func SmallestChange(arr []int) int {
    count := 0
    left := 0
    right := len(arr) - 1

    for left < right {
        if arr[left] != arr[right] {
            count++
            if arr[left] < arr[right] {
                right--
            } else {
                left++
            }
        } else {
            left++
            right--
        }
    }

    return count
}
```

This solution has a time complexity of O(n), where n is the length of the array.