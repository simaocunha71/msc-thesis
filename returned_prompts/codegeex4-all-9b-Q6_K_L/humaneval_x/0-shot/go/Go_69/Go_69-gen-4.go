You can solve this problem by first creating a map to store the frequency of each integer in the list. Then, you can iterate through the map to find the greatest integer that has a frequency greater than or equal to the value of the integer itself.

Here is the solution in Go:

```
func Search(lst []int) int {
    freq := make(map[int]int)
    for _, num := range lst {
        freq[num]++
    }
    max := -1
    for num, count := range freq {
        if count >= num && num > max {
            max = num
        }
    }
    return max
}
```

This solution has a time complexity of O(n), where n is the length of the list.