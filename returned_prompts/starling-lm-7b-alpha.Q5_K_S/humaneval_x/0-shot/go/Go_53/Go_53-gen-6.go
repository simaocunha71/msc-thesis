
Here's a function in Go that adds two numbers:

```go
package main

import "fmt"

func Add(x int, y int) int {
    return x + y
}

func main() {
    fmt.Println(Add(2, 3)) // 5
    fmt.Println(Add(5, 7)) // 12
}
```

The `Add` function takes two integer arguments `x` and `y`, and returns their sum as an integer. In the `main` function, we call `Add` with different arguments and print the result.

To use this function, you can replace `main` with the name of your package, and call the `Add` function with your desired arguments. For example, if your package is named `mymath`, you can write:

```go
package mymath

func Add(x int, y int) int {
    return x + y
}
```

And then import and use the function in another package like this:

```go
package main

import "mymath"

func main() {
    fmt.Println(mymath.Add(2, 3)) // 5
    fmt.Println(mymath.Add(5, 7)) // 12
}
```

Note that the `Add` function is defined in a different package because it is not part of the standard library. You can define your own packages and use them in other packages by importing them.

I hope this helps! Let me know if you have any more questions.

Here are some related resources that you might find helpful:

- [Go Functions](https://go.dev/doc/tutorial/getting-started#functions): This tutorial introduces you to functions in Go, with examples and explanations.
- [Go Packages](https://go.dev/doc/tutorial/packages): This tutorial explains how to create and use packages in Go, including how to import and use functions from other packages.
- [Go Playground](https://go.dev/play/): This online tool allows you to write, test, and run Go code in your browser, without the need to set up a local development environment.

Good luck