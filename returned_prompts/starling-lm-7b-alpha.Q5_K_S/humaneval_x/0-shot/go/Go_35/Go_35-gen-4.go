
Here is one way to solve this problem:

```go
package main

import "fmt"

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

This will output:

```
3
123
```

The `MaxElement` function takes an array of integers as its parameter and returns the maximum element in the array.
It initializes the `max` variable with the first element of the array. Then it iterates through the rest of the elements of the array using a `for` loop.
Inside the loop, it compares each element with the current maximum (`max`). If the current element is greater than the current maximum, it updates the `max` variable.
After the loop is finished, the function returns the maximum element found.
In the `main` function, it calls the `MaxElement` function with two different arrays and prints the result.

Another approach would be to use the `math.Max()` function from the `math` package, which is designed to find the maximum value of a slice of integers or floats. Here is an example of how to use it:

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    fmt.Println(math.Max(1, 2, 3))
    fmt.Println(math.Max(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))
}
```

This will output:

```
3
123
```

The `math.Max()` function takes a variable number of arguments (up to 3) and returns the