Here is the solution in Go:

```go
import (
    "sort"
    "strconv"
)

func UniqueDigits(x []int) []int {
    var result []int
    for _, num := range x {
        str := strconv.Itoa(num)
        hasEvenDigit := false
        for _, c := range str {
            digit, _ := strconv.Atoi(string(c))
            if digit%2 == 0 {
                hasEvenDigit = true
                break
            }
        }
        if !hasEvenDigit {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}
```

This function iterates over the input list `x`. For each number, it checks if the number has any even digit. If not, it appends the number to the `result` list. Finally, it sorts the `result` list in increasing order using `sort.Ints` and returns it.

You can test this function with the examples you provided:

```go
fmt.Println(UniqueDigits([]int{15, 33, 1422, 1})) // [1, 15, 33]
fmt.Println(UniqueDigits([]int{152, 323, 1422, 10})) // []
```



The time complexity of this function is O(n*m), where n is the length of the input list and m is the maximum number of digits in the numbers. The space complexity is O(n), where n is the length of the output list.