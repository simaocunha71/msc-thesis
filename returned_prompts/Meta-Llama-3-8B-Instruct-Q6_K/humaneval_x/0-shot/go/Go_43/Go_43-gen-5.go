```go
func PairsSumToZero(l []int) bool {
    seen := map[int]bool{}
    for _, v := range l {
        if _, ok := seen[-v]; ok {
            return true
        }
        seen[v] = true
    }
    return false
}
```


Explanation:

This function `PairsSumToZero` checks if there are two distinct elements in the list that sum to zero. It does this by iterating over the list and for each element, it checks if its negation is present in the `seen` map. If it is, it returns `true`, indicating that two distinct elements sum to zero. If it iterates over the entire list without finding such a pair, it returns `false`.

The time complexity of this function is O(n), where n is the length of the input list, because it makes a single pass over the list. The space complexity is also O(n), because in the worst case (when all elements are distinct), it needs to store all elements in the `seen` map.