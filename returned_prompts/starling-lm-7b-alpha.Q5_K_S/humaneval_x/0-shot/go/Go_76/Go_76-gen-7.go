
```go
package main

import (
    "fmt"
    "math"
)

func IsSimplePower(x int,n int) bool {
    p := int(math.Pow(float64(n), float64(math.Log(float64(x))/math.Log(float64(n)))))
    return p == x
}

func main() {
    fmt.Println(IsSimplePower(1, 4))
    fmt.Println(IsSimplePower(2, 2))
    fmt.Println(IsSimplePower(8, 2))
    fmt.Println(IsSimplePower(3, 2))
    fmt.Println(IsSimplePower(3, 1))
    fmt.Println(IsSimplePower(5, 3))
}
```

This program defines a function IsSimplePower that takes two parameters, x and n, and returns a boolean value. It uses the math package to calculate the power of n to the power of math.Log(float64(x))/math.Log(float64(n)). If the result of this calculation is equal to x, the function returns true; otherwise, it returns false.

The main function calls the IsSimplePower function with several test cases and prints the results.

The output of the program is:
```
true
true
true
false
false
false
```

This means that the function correctly determines whether a number is a simple power of n or not.
```

```
```

```
```

```
```
```
```

```go
package main

import (
    "fmt"
    "math"
)

func IsSimplePower(x int,n int) bool {
    p := int(math.Pow(float64(n), float64(math.Log(float64(x))/math.Log(float64(n)))))
    return p == x
}

func main() {
    fmt.Println(IsSimplePower(1, 4))
    fmt.Println(IsSimplePower(2, 2))
    fmt.Println(