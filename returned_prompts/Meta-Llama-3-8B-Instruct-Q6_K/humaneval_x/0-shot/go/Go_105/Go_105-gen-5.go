Here is a Go program that implements the described functionality:

```go
package main

import (
    "fmt"
    "sort"
)

var names = []string{"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}

func ByLength(arr []int) []string {
    var result []string
    var valid []int
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            valid = append(valid, num)
        }
    }
    sort.Ints(valid)
    for i := len(valid) - 1; i >= 0; i-- {
        result = append(result, names[valid[i]])
    }
    return result
}

func main() {
    arr := []int{2, 1, 1, 4, 5, 8, 2, 3}
    fmt.Println(ByLength(arr))  // Output: [Eight, Five, Four, Three, Two, Two, One, One]
}
```

In this program, we first filter the array to only include numbers between 1 and 9. We then sort these numbers and reverse them. Finally, we convert each number to its corresponding name and return the result.

The `main` function demonstrates the usage of this program with a sample array. The output is the expected result: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]. If the array is empty, the program will return an empty array. If the array contains any numbers outside the range 1-9, they will be ignored. For example, if the array is `[1, -1, 55]`, the program will return `["One"]`.