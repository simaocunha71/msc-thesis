
To solve this problem, you can use the built-in function `filter()` in Go. The `filter()` function iterates over the input slice (`l`) and returns a new slice with only the values that pass the given condition. In this case, the condition is that the value must be greater than zero (`> 0`).

Here's the code that implements the `GetPositive()` function:

```go
package main

import "fmt"

func GetPositive(l []int) []int {
    return filter(l, func(v int) bool { return v > 0 })
}

func filter(l []int, f func(int) bool) []int {
    r := make([]int, 0, len(l))
    for _, v := range l {
        if f(v) {
            r = append(r, v)
        }
    }
    return r
}
```

You can test the `GetPositive()` function with the provided test cases:

```go
func main() {
    fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6})) // [2, 5, 6]
    fmt.Println(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // [5, 3, 2, 3, 9, 123, 1]
}
```

The `filter()` function is a reusable utility function that takes a slice (`l`) and a function (`f`) as arguments. It creates a new slice (`r`) and iterates over each value (`v`) in the input slice. If the value passes the condition specified by the function (`f(v)`), it is appended to the new slice. Finally, the new slice is returned.

By using the `filter()` function, you can easily create a new slice that only contains the positive values from the input slice.

I hope this helps! Let me know if you have any more questions.

```go
package main

import "fmt