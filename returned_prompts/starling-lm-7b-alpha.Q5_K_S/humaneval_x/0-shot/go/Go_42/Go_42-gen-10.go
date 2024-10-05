
To increment all elements in the list by 1, you can use the `map` function in Go to create a new slice with the incremented values. Here's an example of how you can implement the `IncrList` function:

```go
package main

import "fmt"

func IncrList(l []int) []int {
    return map(l, func(i int) int {
        return i + 1
    })
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3})) // [2, 3, 4]
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123})) // [6, 4, 6, 3, 4, 4, 10, 1, 124]
}
```

In this code, the `IncrList` function takes a slice of integers `l` as input. It uses the `map` function to create a new slice with the same length as `l` and applies the provided function to each element of `l`. The provided function simply adds 1 to each element. The resulting slice with the incremented values is returned by the `IncrList` function.

You can test the `IncrList` function with different input slices by using the `fmt.Println` statements in the `main` function. The output will be the incremented versions of the input slices.

Note that the `map` function in Go is an idiomatic way to perform a transformation on each element of a slice. It takes a slice and a function as arguments, and applies the function to each element of the slice to create a new slice with the transformed values.

I hope this helps! Let me know if you have any more questions.

```go
package main

import "fmt"

func IncrList(l []int) []int {
    return map(l, func(i int) int {
        return i + 1
    })
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3})) // [