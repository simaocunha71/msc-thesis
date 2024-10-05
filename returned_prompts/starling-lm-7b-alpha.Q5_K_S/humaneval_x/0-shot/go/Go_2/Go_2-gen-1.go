    return number - math.Floor(number)


























```
import (
    "math"
)

// Given a positive floating point number, it can be decomposed into
// and integer part (largest integer smaller than given number) and decimals
// (leftover part always smaller than 1).
// 
// Return the decimal part of the number.
// >>> TruncateNumber(3.5)
// 0.5
func TruncateNumber(number float64) float64 {

    return number - math.Floor(number)

}
```
Here's a working solution for the problem:

The `TruncateNumber` function takes a positive floating point number as input and returns the decimal part of the number. It does this by subtracting the largest integer smaller than the given number (obtained using `math.Floor(number)`) from the original number. This ensures that the result is always less than 1.

For example, when `TruncateNumber(3.5)` is called, it will return `0.5` as the decimal part of the number.

To use the function, you can simply call it with the desired number as an argument. In this case, the function call `TruncateNumber(3.5)` will return `0.5`.

Here's a sample code snippet demonstrating the usage of the `TruncateNumber` function:

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    number := 3.5
    decimalPart := TruncateNumber(number)
    fmt.Println(decimalPart) // Output: 0.5
}
```

By using the `TruncateNumber` function, you can easily extract the decimal part of a positive floating point number in Go.

```

```

```

```

```

```

```

```

```

```

```

```

```

```
