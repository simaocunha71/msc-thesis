
To solve this problem you can use the Euclidean algorithm. It is a method to find the greatest common divisor (GCD) of two numbers. Here's a step-by-step explanation of the algorithm:

1. If either of the numbers is zero, the GCD is the nonzero number.
2. If the remainder of dividing the larger number by the smaller number is zero, then the GCD is the smaller number. Otherwise, go back to step 1 with the smaller number and the remainder.
3. Repeat step 2 until the remainder is zero. The GCD is the last nonzero remainder.

Here's the Go code to implement the Euclidean algorithm:

```go
package main

import "fmt"

func GreatestCommonDivisor(a, b int) int {
    for b != 0 {
        t := b
        b = a % b
        a = t
    }
    return a
}

func main() {
    fmt.Println(GreatestCommonDivisor(3, 5))
    fmt.Println(GreatestCommonDivisor(25, 15))
}
```

When you run this code, it will output:

```
1
5
```

In the `GreatestCommonDivisor` function, we use a `for` loop to repeatedly update `a` and `b` using the Euclidean algorithm until `b` becomes zero. Then we return the last nonzero value of `a`, which is the GCD of the original `a` and `b`.

The `main` function simply calls `GreatestCommonDivisor` with two sample inputs and prints the results.

Hope this helps! Let me know if you have any more questions.

```go
package main

import "fmt"

func GreatestCommonDivisor(a, b int) int {
    for b != 0 {
        t := b
        b = a % b
        a = t
    }
    return a
}

func main() {
    fmt.Println(GreatestCommonDivisor(3, 5))
    fmt.Println(GreatestCommonDivisor(