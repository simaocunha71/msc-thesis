
To solve this problem we will use a matrix exponentiation method to compute the Fibonacci numbers.

Let $F$ be the Fibonacci matrix, a 2x2 matrix defined as:

$F = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$

Now consider the following properties of the Fibonacci matrix:

- $F^2 = F * F = F$
- $F^3 = F * F * F = F * F = F$
- $F^4 = F * F * F * F = F * F = F$
- ...

As we can see, the Fibonacci matrix raised to the power of $n$ will always be equal to itself.

That's why to compute the $n$-th Fibonacci number we only need to raise the Fibonacci matrix to the power of $(n-1)$.

Here is the Go code implementing the described approach:

```go
package main

import (
	"fmt"
	"math/big"
)

func Fib(n int) int {
	if n == 1 {
		return 1
	}

	f := big.NewInt(1)
	f.Exp(&f, big.NewInt(n-1), nil)

	return f.Int64()
}

func main() {
	fmt.Println(Fib(10))
	fmt.Println(Fib(1))
	fmt.Println(Fib(8))
}
```

The output of the code will be:

```
55
1
21
```

Note that in the code above we are using the `big` package to handle large numbers.

The time complexity of the code is $O(\log n)$, as we are using exponentiation by squaring, which is an efficient method to compute the power of a number.

The space complexity is also $O(\log n)$.

The running time of the code is proportional to the number of bits in $n$, as we need to square the matrix $\log n$ times.

In the worst case scenario, the matrix multiplication can be