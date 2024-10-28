Here is a possible implementation of the `TotalMatch` function in Go:
```go
func TotalMatch(lst1 []string, lst2 []string) []string {
    total1 := 0
    total2 := 0
    for _, s1 := range lst1 {
        total1 += len(s1)
    }
    for _, s2 := range lst2 {
        total2 += len(s2)
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
Here's an explanation of the code:

1. We initialize two variables `total1` and `total2` to 0, which will store the total number of characters in each list.
2. We iterate over each string in `lst1` and add its length to `total1`.
3. We iterate over each string in `lst2` and add its length to `total2`.
4. We compare the two totals. If `total1` is less than `total2`, we return `lst1`. If `total1` is greater than `total2`, we return `lst2`. If the two totals are equal, we return `lst1` since the problem statement asks to return the first list in case of a tie.

You can test this function with the examples you provided to see that it returns the correct result.