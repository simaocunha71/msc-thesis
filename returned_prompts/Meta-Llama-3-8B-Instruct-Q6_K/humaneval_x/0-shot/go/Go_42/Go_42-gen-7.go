```go
package main

import (
    "fmt"
)

func IncrList(l []int) []int {
    result := make([]int, len(l))
    for i, v := range l {
        result[i] = v + 1
    }
    return result
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3})) // [2, 3, 4]
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123})) // [6, 4, 6, 3, 4, 4, 10, 1, 124]
}
```



The solution above is a simple function that takes a slice of integers as input and returns a new slice where each element is incremented by 1. It uses a for loop to iterate over the input slice, adding 1 to each element and storing the result in a new slice. This new slice is then returned as the output. The function is tested in the main function with two examples. The output is printed to the console. The time complexity of this solution is O(n), where n is the length of the input slice, because it iterates over the slice once. The space complexity is also O(n), because it creates a new slice to store the output. This solution is efficient and easy to understand.