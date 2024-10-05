You can solve this problem by iterating through the list and checking if each number is less than the next one. If you find a number that is not less than the next one, or if you find a duplicate, return false. If you get through the entire list without finding a problem, return true.

Here's a possible solution in Go:

```go
func IsSorted(lst []int) bool {
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] >= lst[i+1] {
            return false
        }
    }
    return true
}
```

This solution iterates through the list once, so it has a time complexity of O(n), where n is the length of the list.