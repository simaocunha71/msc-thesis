
Here is a working solution in Go:

```go
package main

import "fmt"

func IncrList(l []int) []int {
    out := make([]int, len(l))
    for i, v := range l {
        out[i] = v + 1
    }
    return out
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3}))
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123}))
}
```

This code defines a function called `IncrList` that takes a slice of integers as an argument and returns a new slice of integers with each element incremented by one. It does this by creating a new slice of the same length as the input slice, and then iterating over the input slice using the `range` keyword. For each element in the input slice, it adds one and stores the result in the corresponding position in the output slice. Finally, it returns the output slice.

In the `main` function, the `IncrList` function is called with two different input slices, and the results are printed to the console.

The output of this code will be:

```
[2 3 4]
[6 4 6 3 4 4 10 1 124]
```

As you can see, each element in the input slices has been incremented by one in the output slices.

You can try this code in the Go Playground by following this link: [Go Playground](https://play.golang.org/p/6_YsE3X3hX)

I hope this helps! Let me know if you have any more questions.

// Return list with elements incremented by 1.
// >>> IncrList([1, 2, 3])
// [2, 3, 4]
// >>> IncrList([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [6, 4, 6, 3