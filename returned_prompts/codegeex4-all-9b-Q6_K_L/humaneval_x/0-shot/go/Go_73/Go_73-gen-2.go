To solve this problem, we need to compare the elements from the start and end of the array. If they are not equal, we need to change one of them to make them equal. We can keep track of the number of changes made and return it as the result.

Here is the step-by-step algorithm:
1. Initialize a variable count to 0 to keep track of the number of changes made.
2. Iterate over the array from index 0 to the middle index.
3. Compare the element at the current index with the element at the corresponding index from the end of the array.
4. If they are not equal, increment the count by 1 and change one of them to make them equal.
5. Return the count as the result.

Here is the implementation of the algorithm in Go:

```go
func SmallestChange(arr []int) int {
    count := 0
    length := len(arr)
    mid := length / 2

    for i := 0; i < mid; i++ {
        if arr[i] != arr[length-i-1] {
            count++
            if arr[i] > arr[length-i-1] {
                arr[i] = arr[length-i-1]
            } else {
                arr[length-i-1] = arr[i]
            }
        }
    }

    return count
}
```

This solution has a time complexity of O(n), where n is the length of the array.