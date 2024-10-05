To determine whether there exist two distinct elements in the list that sum to zero, you can use a map to store the elements as you iterate through the list. This way, you can check if the negative of the current element exists in the map. If it does, then there are two distinct elements that sum to zero. Otherwise, you add the current element to the map and continue. Here's the modified code:

```go
func PairsSumToZero(l []int) bool {
    seen := make(map[int]struct{}, len(l))
    for _, num := range l {
        if _, exists := seen[-num]; exists {
            return true
        }
        seen[num] = struct{}{}
    }
    return false
}
```

This code initializes an empty map `seen` to keep track of the elements seen so far. It then iterates through the input list `l`. For each element `num`, it checks if the negative of `num` exists in the map `seen`. If it does, it means there are two distinct elements in the list that sum to zero, so the function returns `true`. Otherwise, it adds `num` to the map `seen` and continues. If the loop completes without finding any such pair, the function returns `false`.