
Here's the Go code for the IncrList function:

```go
package main

import "fmt"

func IncrList(l []int) []int {
    for i := 0; i < len(l); i++ {
        l[i]++
    }
    return l
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3}))
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123}))
}
```

This will output:

```
[2, 3, 4]
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```

In the code, the function `IncrList` takes a slice of integers `l` as an argument and returns a new slice with the same elements incremented by 1. It does this by iterating through the input slice using a for loop and incrementing each element by 1 using the `++` operator. The modified slice is then returned.

In the `main` function, we call the `IncrList` function with two example slices and print the results using the `fmt.Println` function.

You can try running this code on the Go Playground by following this link: [Go Playground](https://play.golang.org/p/r7Dj7X7-rZ)

I hope this helps! Let me know if you have any further questions.

```go
package main

import "fmt"

func IncrList(l []int) []int {
    for i := 0; i < len(l); i++ {
        l[i]++
    }
    return l
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3}))
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123}))
}
```