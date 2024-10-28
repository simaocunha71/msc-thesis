The problem is asking for the greatest integer that appears in the list at least as many times as its value. If no such integer exists, the function should return -1.

Here's a solution in Go:

```go
func Search(lst []int) int {
    frequency := make(map[int]int)
    max := -1

    for _, num := range lst {
        frequency[num]++
        if frequency[num] >= num && num > max {
            max = num
        }
    }

    return max
}
```

In this solution, we first create a map called `frequency` to store the frequency of each integer in the list. Then, we iterate over the list and update the frequency of each integer in the map. 

After that, for each integer in the map, we check if its frequency is greater than or equal to its value and if it's greater than the current maximum value `max`. If both conditions are true, we update `max` to this integer.

Finally, we return the value of `max`. If `max` is still -1, it means no such integer exists in the list, so we return -1.