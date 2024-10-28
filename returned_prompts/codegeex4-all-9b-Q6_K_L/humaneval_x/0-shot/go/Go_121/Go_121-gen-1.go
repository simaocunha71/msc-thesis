This problem requires a sum of all odd elements that are in even positions. This means that every other element in the list, starting from the second one, should be checked.

Here's how you can implement this in Go:

```go
func Solution(lst []int) int {
    sum := 0
    for i := 1; i < len(lst); i += 2 {
        if lst[i]%2 != 0 {
            sum += lst[i]
        }
    }
    return sum
}
```

This function uses a for loop to iterate over the list, skipping every other element (i+=2). For each element, it checks if it's odd (lst[i]%2 != 0). If it is, it adds the element to the sum. Finally, it returns the sum.

This solution has a time complexity of O(n) where n is the length of the list, as it needs to iterate over each element once.