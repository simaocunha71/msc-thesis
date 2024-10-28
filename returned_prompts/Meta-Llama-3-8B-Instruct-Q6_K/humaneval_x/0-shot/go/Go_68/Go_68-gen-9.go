Here is the solution in Go:
```go
func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }
    minEven := math.MaxInt
    minIndex := -1
    for i, v := range arr {
        if v%2 == 0 && v < minEven {
            minEven = v
            minIndex = i
        }
    }
    if minIndex == -1 {
        return []int{}
    }
    return []int{minEven, minIndex}
}
```
Here's an explanation of the solution:

1. First, we check if the input array is empty. If it is, we return an empty list `[]int{}`.
2. We initialize `minEven` to the maximum possible integer value `math.MaxInt` and `minIndex` to -1. These will be used to store the smallest even value and its index.
3. We iterate over the input array using a range-based for loop. For each element `v` at index `i`, we check if it's an even number (`v % 2 == 0`) and if it's smaller than the current `minEven`. If it is, we update `minEven` and `minIndex` accordingly.
4. After the loop, we check if `minIndex` is still -1. If it is, it means we didn't find any even numbers in the array, so we return an empty list `[]int{}`.
5. Otherwise, we return a list containing the smallest even value `minEven` and its index `minIndex`.

This solution has a time complexity of O(n), where n is the length of the input array, since we iterate over the array once. The space complexity is O(1) since we only use a few extra variables to store the minimum even value and its index.