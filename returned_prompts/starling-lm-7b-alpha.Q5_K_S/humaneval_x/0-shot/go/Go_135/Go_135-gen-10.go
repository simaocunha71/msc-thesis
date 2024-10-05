
    index := 0
    for i := 1; i < len(arr); i++ {
        if arr[i] > arr[index] {
            index = i
        }
    }
    if index == 0 {
        return -1
    }
    for i := index - 1; i >= 0; i-- {
        if arr[i] >= arr[index] {
            index = i
        }
    }
    return index
}

*/

package main

import "fmt"

func main() {
    arr := []int{1, 2, 4, 3, 5}
    index := CanArrange(arr)
    fmt.Println(index)

    arr = []int{1, 2, 3}
    index = CanArrange(arr)
    fmt.Println(index)
}
```

This code defines a function `CanArrange` which finds the largest index of an element which is not greater than or equal to the element immediately preceding it. If no such element exists, it returns -1. The function iterates through the array to find the largest index where the condition is met, and then checks the previous elements to ensure the condition is still met. Finally, it returns the largest index that satisfies the condition.

In the `main` function, the `CanArrange` function is tested with two example arrays. The first array `[1, 2, 4, 3, 5]` has an expected output of `3`, as the element at index `3` is not greater than or equal to the element at index `2`. The second array `[1, 2, 3]` has an expected output of `-1`, as no element is greater than or equal to the element immediately preceding it.

The code is written in Go programming language, and it uses the `fmt` package to print the output.

*/

```go
package main

import "fmt"

func CanArrange(arr []int) int {
    index := 0
    for i := 1; i < len(arr); i++ {
        if arr[i] > arr[index] {
            index = i
        }
   