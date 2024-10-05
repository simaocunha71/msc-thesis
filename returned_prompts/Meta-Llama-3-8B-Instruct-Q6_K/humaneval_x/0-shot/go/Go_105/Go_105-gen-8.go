Here is a Go function that implements the problem description:
```go
func ByLength(arr []int) []string {
    var result []string
    var sorted []int
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            sorted = append(sorted, num)
        }
    }
    sort.Ints(sorted)
    for _, num := range sorted {
        switch num {
        case 1:
            result = append(result, "One")
        case 2:
            result = append(result, "Two")
        case 3:
            result = append(result, "Three")
        case 4:
            result = append(result, "Four")
        case 5:
            result = append(result, "Five")
        case 6:
            result = append(result, "Six")
        case 7:
            result = append(result, "Seven")
        case 8:
            result = append(result, "Eight")
        case 9:
            result = append(result, "Nine")
        }
    }
    reverse(result)
    return result
}

func reverse(s []string) {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
}
```
Here's a breakdown of how the function works:

1. It first iterates over the input array, filtering out numbers outside the range 1-9 and storing the remaining numbers in a separate slice `sorted`.
2. It then sorts the `sorted` slice in ascending order using the `sort.Ints` function.
3. It iterates over the sorted slice, replacing each number with its corresponding name using a switch statement.
4. It appends the resulting names to a new slice `result`.
5. Finally, it reverses the `result` slice using a helper function `reverse`.
6. The function returns the resulting slice of strings.

Note that this function assumes that the input array contains only integers, and that the integers are between 1 and 9 inclusive. If the input array contains non-integer values or values outside this range, the function may not work correctly. You may want to add additional error handling or input validation to handle these cases.