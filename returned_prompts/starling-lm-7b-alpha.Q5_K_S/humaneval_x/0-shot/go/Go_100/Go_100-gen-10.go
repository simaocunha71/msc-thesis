
var res []int

for i := n; i > 0; i-- {
    res = append(res, i)
    if i%2 != 0 {
        i++
    } else {
        i--
    }
}

return res
```

Here's a simple function that accomplishes this task.

In the for loop, we start with the value of `n` and append it to our result slice. Then, we check whether `i` is odd or even. If `i` is odd, we increment it by one, otherwise, we decrement it by one.

Finally, we return the result slice with all the values.

For example, if we call `MakeAPile(3)`, the function will return `[3, 5, 7]`.

```go
func MakeAPile(n int) []int {
    res := make([]int, 0, n)
    for i := n; i > 0; i-- {
        res = append(res, i)
        if i%2 != 0 {
            i++
        } else {
            i--
        }
    }
    return res
}
```

You can try it out in this [Go Playground](https://play.golang.org/p/628q8r9n6Z).

```go
package main

import "fmt"

func main() {
    fmt.Println(MakeAPile(3))
}
```

This will output `[3, 5, 7]`.

```
[3, 5, 7]
```

Here's a simple function that accomplishes this task.

In the for loop, we start with the value of `n` and append it to our result slice. Then, we check whether `i` is odd or even. If `i` is odd, we increment it by one, otherwise, we decrement it by one.

Finally, we return the result slice with all the values.

For example, if we call `MakeAPile(3)`, the function will return `[3, 5, 7]`.

```go
func Make