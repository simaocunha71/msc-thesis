```go
func Solution(lst []int) int {
    var sum int
    for i, val := range lst {
        if i%2 == 0 && val%2 != 0 {
            sum += val
        }
    }
    return sum
}
```



Explanation:

This Go function, `Solution`, takes a slice of integers `lst` as input and returns the sum of all odd elements in even positions. 

The function iterates over the input slice using a range-based loop. For each element `val` at index `i`, it checks two conditions:
- `i%2 == 0`: This ensures that the current index is even.
- `val%2 != 0`: This ensures that the current element is odd.

If both conditions are met, it adds the element to the `sum`. 

Finally, the function returns the calculated sum. 

For example, if the input slice is `[5, 8, 7, 1]`, the function will add `5` and `7` (which are odd elements at even positions) to the sum, resulting in `12`. 

The function has a time complexity of O(n), where n is the length of the input slice, as it needs to iterate over the entire slice once. The space complexity is O(1), as it only uses a constant amount of space to store the sum. 