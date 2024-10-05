You can use the following code to solve the problem:

```go
func CanArrange(arr []int) int {
    for i := 1; i < len(arr); i++ {
        if arr[i-1] >= arr[i] {
            return i-1
        }
    }
    return -1
}
```

Explanation:
The function `CanArrange` takes an array of integers as input and returns the largest index of an element which is not greater than or equal to the element immediately preceding it. If no such element exists then it returns -1.

The function iterates through the array starting from the second element. If the current element is less than or equal to the previous element, it returns the index of the previous element. If no such element is found, it returns -1.

This solution has a time complexity of O(n), where n is the length of the array.