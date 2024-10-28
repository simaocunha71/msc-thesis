
To return the maximum element of a slice, you can use the `max` function from the `math` package. Here's an example of how you can use it:

```go
package main

import (
    "fmt"
    "math"
)

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    list := []int{1, 2, 3}
    fmt.Println(MaxElement(list)) // prints 3

    list = []int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}
    fmt.Println(MaxElement(list)) // prints 123
}
```

In this example, we define a `max` function that compares two integers and returns the larger one. We then use this function within the `MaxElement` function to find the maximum element in the input slice. Finally, we test the `MaxElement` function with two example slices and print the results.

Note that the `MaxElement` function is not optimized for slices with a large number of elements. If you have a slice with a large number of elements, you may want to use other methods like the `sort` package to find the maximum element more efficiently.

Additionally, you can use the `math.Max` function to find the maximum value among multiple integers. Here's an example of how you can use it:

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    max := math.Max(1, 2, 3)
    fmt.Println(max) // prints 3

    max = math.Max(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10)
    fmt.Println(max) // prints 123
}
```

In this example, we use the `math.Max` function to find the maximum value among multiple integers. We pass the integers as arguments