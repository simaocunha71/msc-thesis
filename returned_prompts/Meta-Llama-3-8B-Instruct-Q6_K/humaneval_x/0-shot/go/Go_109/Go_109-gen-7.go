Here is a solution to the problem:

```go
func MoveOneBall(arr []int) bool {
    if len(arr) == 0 {
        return true
    }
    var sortedArr []int
    for len(arr) > 0 {
        last := arr[len(arr)-1]
        arr = arr[:len(arr)-1]
        for i, val := range arr {
            if val > last {
                arr[i], last = last, val
                break
            }
        }
        sortedArr = append(sortedArr, last)
    }
    return sort.IntsEqual(sortedArr, arr)
}
```

Explanation:

The solution works by simulating the right shift operation and checking if the resulting array is sorted. Here's a step-by-step breakdown:

1. If the input array is empty, return true as there are no elements to sort.
2. Initialize an empty slice `sortedArr` to store the sorted elements.
3. Loop until the input array is empty.
4. In each iteration, pop the last element from the input array and append it to `sortedArr`.
5. Then, iterate through the remaining elements in the input array and find the first element that is greater than the last element popped. Swap this element with the last element popped.
6. Repeat step 4 until the input array is empty.
7. Finally, check if the `sortedArr` is equal to the original array. If it is, return true, indicating that the original array can be sorted by performing right shift operations. Otherwise, return false. The `sort.IntsEqual` function is used to compare the two arrays.

The time complexity of this solution is O(n^2) due to the nested loops, where n is the length of the input array. The space complexity is O(n) for storing the sorted array. However, this solution is not efficient for large input arrays. A more efficient solution could be achieved by using a different approach, such as using a priority queue or a heap data structure.