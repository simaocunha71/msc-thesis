Here is the solution in Go:

```go
package main

import (
    "fmt"
    "sort"
)

func main() {
    arr := []int{2, 1, 1, 4, 5, 8, 2, 3}
    fmt.Println(ByLength(arr))
}

func ByLength(arr []int) []string {
    var result []string
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] < arr[j]
    })
    for _, v := range arr {
        if v >= 1 && v <= 9 {
            result = append(result, names[v])
        }
    }
    for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
        result[i], result[j] = result[j], result[i]
    }
    return result
}

var names = [...]string{
    "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
}
```

In this code, the function `ByLength` takes an array of integers as input, sorts the array, filters the numbers from 1 to 9, replaces each number with its corresponding name, and then reverses the result. The `main` function demonstrates the usage of the `ByLength` function. The `names` variable is an array of strings representing the names of numbers from 0 to 9. The `sort.Slice` function is used to sort the input array. The `append` function is used to add the names to the result array. The `for` loop is used to reverse the result array. The function returns the result array. If the input array is empty, the function returns an empty array. If the input array contains any numbers outside the range 1 to 9, they are ignored. The function also ignores any non-integer values in the input array.