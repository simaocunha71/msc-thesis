```go
package main

import "fmt"

func IncrList(l []int) []int {
    result := make([]int, len(l))
    for i, v := range l {
        result[i] = v + 1
    }
    return result
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3}))  // [2 3 4]
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123})) // [6 4 6 3 4 4 10 1 124]
}
```


The code defines a function `IncrList` that takes a slice of integers `l` as input and returns a new slice where each element is incremented by 1. The function uses a loop to iterate over the elements of the input slice, adding 1 to each element and storing the result in a new slice. The function returns this new slice.

In the `main` function, we test the `IncrList` function with two example inputs. The first input is `[1, 2, 3]`, which is incremented to `[2, 3, 4]`. The second input is a longer slice with more varied elements, which is incremented to `[6, 4, 6, 3, 4, 4, 10, 1, 124]`. We use the `fmt.Println` function to print the results to the console.