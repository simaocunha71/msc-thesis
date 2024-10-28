Here is a Go function that solves the problem:

```go
func TotalMatch(lst1 []string, lst2 []string) []string {
    var total1 int
    var total2 int

    for _, str := range lst1 {
        total1 += len(str)
    }
    for _, str := range lst2 {
        total2 += len(str)
    }

    if total1 < total2 {
        return lst1
    } else if total1 > total2 {
        return lst2
    } else {
        return lst1
    }
}
```

This function calculates the total number of characters in each list and compares them. If the total number of characters in `lst1` is less than `lst2`, it returns `lst1`. If the total number of characters in `lst2` is less than `lst1`, it returns `lst2`. If the two lists have the same total number of characters, it returns `lst1` because the problem states to return the first list in case of a tie.