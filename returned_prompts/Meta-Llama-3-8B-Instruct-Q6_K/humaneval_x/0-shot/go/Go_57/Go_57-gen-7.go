```go
package main

import (
    "fmt"
)

func Monotonic(l []int) bool {
    increasing := true
    decreasing := true
    for i := 1; i < len(l); i++ {
        if l[i] > l[i-1] {
            decreasing = false
        }
        if l[i] < l[i-1] {
            increasing = false
        }
    }
    return increasing || decreasing
}

func main() {
    fmt.Println(Monotonic([]int{1, 2, 4, 20})) // true
    fmt.Println(Monotonic([]int{1, 20, 4, 10})) // false
    fmt.Println(Monotonic([]int{4, 1, 0, -10})) // true
}
```


Explanation:
The function Monotonic checks if a given list is either monotonically increasing or decreasing. It initializes two boolean variables, increasing and decreasing, to true. Then, it iterates over the list, starting from the second element (index 1). For each element, it checks if it's greater than the previous one. If it is, it sets decreasing to false. If it's smaller, it sets increasing to false. After checking all elements, it returns true if either increasing or decreasing is still true, indicating that the list is monotonically increasing or decreasing. If both are false, it returns false, indicating that the list is neither increasing nor decreasing. In the main function, we test the Monotonic function with three different lists and print the results.