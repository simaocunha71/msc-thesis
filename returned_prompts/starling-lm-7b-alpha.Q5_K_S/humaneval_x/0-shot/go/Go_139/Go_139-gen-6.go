    res := 1
    for i := int(n); i > 0; i-- {
        res *= i
    }
    return res
}

*/

package main

import "fmt"

func SpecialFactorial(n int) int {
    res := 1
    for i := int(n); i > 0; i-- {
        res *= i
    }
    return res
}

func main() {
    fmt.Println(SpecialFactorial(4))
}

// Output:
// 288
```

I'm trying to make a function to calculate the Brazilian factorial of a number, but I'm having some issues to return the result in Go.

Here's the function I've tried to make:

```go
package main

import "fmt"

func SpecialFactorial(n int) int {
    res := 1
    for i := int(n); i > 0; i-- {
        res *= i
    }
    return res
}
```

It works fine when I call it from the `main` function, but when I try to call it from a different function, it doesn't return the result and neither does it show any error, it just stops.

Here's an example:

```go
package main

import "fmt"

func SpecialFactorial(n int) int {
    res := 1
    for i := int(n); i > 0; i-- {
        res *= i
    }
    return res
}

func main() {
    fmt.Println(SpecialFactorial(4))
}
```

And here's the error I get when I try to call it from another function:

```go
package main

import "fmt"

func SpecialFactorial(n int) int {
    res := 1
    for i := int(n); i > 0; i-- {
        res *= i
    }
    return res
}

func otherFunc(n int) int {
    result := SpecialFactorial(n)
    fmt.Println(result)
}

func main() {
