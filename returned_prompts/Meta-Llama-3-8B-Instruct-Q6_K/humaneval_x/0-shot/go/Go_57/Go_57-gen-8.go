```go
func Monotonic(l []int) bool {
    increasing := true
    decreasing := true
    for i := 1; i < len(l); i++ {
        if l[i] > l[i-1] {
            decreasing = false
        } else if l[i] < l[i-1] {
            increasing = false
        }
    }
    return increasing || decreasing
}
```



Here is the explanation of the code:

1. Initialize two boolean variables `increasing` and `decreasing` to `true`. This is because initially, we don't know the trend of the list, so we assume it's either increasing or decreasing.

2. Loop through the list starting from the second element (index 1) to the end. For each element, check if it's greater than the previous element. If it is, then `decreasing` becomes `false` because the list is no longer decreasing.

3. If the current element is less than the previous element, then `increasing` becomes `false` because the list is no longer increasing.

4. After looping through the entire list, check if either `increasing` or `decreasing` is still `true`. If either of them is `true`, it means the list is either increasing or decreasing, so return `true`. Otherwise, return `false`.

This function works because it checks for both increasing and decreasing trends in the list. If the list is either increasing or decreasing, the function will return `true`. If the list is neither increasing nor decreasing, the function will return `false`.