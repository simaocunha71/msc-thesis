```go
package main

import "fmt"

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
    fmt.Println(Monotonic([]int{1, 2, 4, 20}))  // true
    fmt.Println(Monotonic([]int{1, 20, 4, 10})) // false
    fmt.Println(Monotonic([]int{4, 1, 0, -10})) // true
}
```


The function Monotonic checks if a list of integers is either monotonically increasing or decreasing. It initializes two boolean variables, increasing and decreasing, both set to true. It then iterates over the list, checking if each element is greater than the previous one (decreasing) or less than the previous one (increasing). If it finds an element that doesn't fit the pattern, it sets the corresponding boolean variable to false. Finally, it returns whether the list is either increasing or decreasing.

The main function demonstrates the usage of the Monotonic function with three different lists. The output of these examples is as expected: the first list is monotonically increasing, the second is not, and the third is monotonically decreasing.