You can use the following code to solve the problem:

```
func Solution(lst []int) int {
    sum := 0
    for i := 0; i < len(lst); i += 2 {
        if lst[i]%2 != 0 {
            sum += lst[i]
        }
    }
    return sum
}
```

This code iterates over the list in steps of 2 (starting from index 0), and adds the value of the current element to the sum if it is odd. Finally, it returns the sum.