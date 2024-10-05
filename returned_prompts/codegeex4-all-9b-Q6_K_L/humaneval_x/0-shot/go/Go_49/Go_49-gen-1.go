You can use the built-in function `math.Pow` to calculate 2^n. Then, use the `math.Mod` function to get the modulo of the result and p.

Here is the corrected code:

```go
package kata

import (
	"math"
)

func Modp(n int, p int) int {
	return int(math.Mod(math.Pow(2, float64(n)), float64(p)))
}
```

The `math.Pow` function takes two arguments: the base and the exponent. In this case, the base is 2 and the exponent is `float64(n)`. The `math.Mod` function takes two arguments: the number to be divided and the divisor. In this case, the number to be divided is the result of `math.Pow` and the divisor is `float64(p)`. The `int` function is used to convert the result to an integer.