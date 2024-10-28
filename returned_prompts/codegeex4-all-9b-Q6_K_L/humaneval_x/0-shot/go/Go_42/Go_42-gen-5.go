You can create a new list with the incremented values and return it. Here is how you can do it:

```go
func IncrList(l []int) []int {
    newList := make([]int, len(l))
    for i, v := range l {
        newList[i] = v + 1
    }
    return newList
}
```

In this code, we first create a new list `newList` with the same length as the input list `l`. Then we iterate over the input list with `range`, and for each element, we add 1 and assign it to the corresponding position in `newList`. Finally, we return `newList`.