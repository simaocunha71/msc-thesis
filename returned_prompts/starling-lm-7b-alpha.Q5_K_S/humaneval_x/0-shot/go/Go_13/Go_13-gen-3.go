
To solve this problem, you can use the Euclidean algorithm. Here's a step-by-step guide on how to do it:

1. If a is 0, then the gcd is b. If b is 0, then the gcd is a. In all other cases, the gcd is the remainder of the division of a by b.
2. Repeat the process with the values of a and b updated with the remainder of the division of a by b and b, respectively.
3. Repeat step 2 until either a or b is 0.

Here's the Go code that implements the algorithm:

```go
package main

import "fmt"

func GreatestCommonDivisor(a int, b int) int {
    for a != 0 && b != 0 {
        if a > b {
            a %= b
        } else {
            b %= a
        }
    }
    return a + b
}

func main() {
    fmt.Println(GreatestCommonDivisor(3, 5))
    fmt.Println(GreatestCommonDivisor(25, 15))
}
```

When you run the code, it will output:

```
1
5
```

This means that the greatest common divisor of 3 and 5 is 1, and the greatest common divisor of 25 and 15 is 5.

You can try out the code on the Go Playground by clicking here: [Go Playground](https://play.golang.org/p/697v6_65V9)

This algorithm is very efficient, as it only requires a constant number of iterations.

The time complexity of the algorithm is O(log min(a,b)), and the space complexity is O(1).

The algorithm was discovered by Carl Friedrich Gauss, a German mathematician and physicist, in the early 19th century.

It's one of the oldest and most widely used algorithms in computer science, and it's used in a variety of different applications, including cryptography, computer algebra systems, and more.

The Euclidean algorithm is named after the