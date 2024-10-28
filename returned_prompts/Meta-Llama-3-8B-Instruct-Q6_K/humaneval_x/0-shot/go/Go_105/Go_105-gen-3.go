Here is the solution in Go:
```go
func ByLength(arr []int) []string {
    // Filter out numbers outside the range [1, 9]
    filtered := make([]int, 0)
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filtered = append(filtered, num)
        }
    }

    // Sort the filtered array
    sort.Ints(filtered)

    // Reverse the sorted array
    reverse := make([]int, len(filtered))
    copy(reverse, filtered)
    for i := 0; i < len(reverse); i++ {
        reverse[i] = filtered[len(filtered)-1-i]
    }

    // Map each digit to its corresponding name
    result := make([]string, len(reverse))
    for i, num := range reverse {
        switch num {
        case 1:
            result[i] = "One"
        case 2:
            result[i] = "Two"
        case 3:
            result[i] = "Three"
        case 4:
            result[i] = "Four"
        case 5:
            result[i] = "Five"
        case 6:
            result[i] = "Six"
        case 7:
            result[i] = "Seven"
        case 8:
            result[i] = "Eight"
        case 9:
            result[i] = "Nine"
        default:
            result[i] = ""
        }
    }

    return result
}
```
Here's an explanation of the code:

1. We filter out numbers outside the range [1, 9] and store them in a new array `filtered`.
2. We sort the `filtered` array using the `sort.Ints` function.
3. We reverse the sorted array using a temporary array `reverse`.
4. We map each digit in the `reverse` array to its corresponding name using a `switch` statement.
5. We return the resulting array of strings.

You can test this function with the example input you provided:
```go
arr := []int{2, 1, 1, 4, 5, 8, 2, 3}
result := ByLength(arr)
fmt.Println(result) // Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
```