You are computing 2^n % p, which is equivalent to the remainder of the division of 2^n by p. The Go language provides the operator % for computing the remainder of a division.

The pow() function from the math package computes 2^n.

Here is the solution:

```go
package kata

import "math"

func Modp(n int, p int) int {
    return int(math.Pow(2, float64(n)) % float64(p))
}
```