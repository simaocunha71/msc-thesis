You can solve this problem in Golang by using the built-in map type to keep track of the count of each element in the list. Here is a possible solution:

```go
func IncrList(l []int) []int {
    count := make(map[int]int)
    for _, num := range l {
        count[num]++
    }
    result := make([]int, 0)
    for num := range count {
        if count[num] > 0 {
            result = append(result, num)
            count[num]--
        }
    }
    return result
}
```

This solution first counts the occurrence of each number in the list and then creates a new list with the numbers in the same order as they appear in the original list, but with each number repeated as many times as it appears in the original list.

This solution has a time complexity of O(n), where n is the length of the input list.