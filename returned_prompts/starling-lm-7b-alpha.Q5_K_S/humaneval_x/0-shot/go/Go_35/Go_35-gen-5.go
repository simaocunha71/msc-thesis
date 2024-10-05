
Here's a Go program that implements the `MaxElement` function:

```go
package main

import (
    "fmt"
)

func MaxElement(l []int) int {
    max := l[0]
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
}

func main() {
    fmt.Println(MaxElement([]int{1, 2, 3}))
    fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}
```

Explanation:

The `MaxElement` function takes a slice of integers as an argument and returns the maximum element in the slice. It initializes the `max` variable with the first element of the slice. Then, it iterates through the rest of the elements in the slice using a `for` loop. Inside the loop, it compares each element with the current maximum value (`max`). If the element is greater than the current maximum, it updates the `max` variable with the new maximum value. Finally, it returns the maximum value after the loop is finished.

In the `main` function, we call the `MaxElement` function with two different slices of integers (`[1, 2, 3]` and `[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]`). The program then prints the maximum element of each slice using the `fmt.Println` function.

When you run the program, it will output:

```
3
123
```

These are the maximum elements in the provided slices.

You can test the program with different input slices to see how it works.

```go
package main

import (
    "fmt"
)

func MaxElement(l []int) int {
    max := l[0]
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return