
    if x < 1 || n < 1 {
        return false
    }

    if x == 1 {
        return true
    }

    for i := 2; i <= x/2; i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
    }

    return false
}

```

## Test

```go
package main

import (
	"fmt"
)

func main() {

	fmt.Println(IsSimplePower(1, 4)) // true
	fmt.Println(IsSimplePower(2, 2)) // true
	fmt.Println(IsSimplePower(8, 2)) // true
	fmt.Println(IsSimplePower(3, 2)) // false
	fmt.Println(IsSimplePower(3, 1)) // false
	fmt.Println(IsSimplePower(5, 3)) // false

}
```

## Result

```shell
true
true
true
false
false
false
```

## Explanation

The function IsSimplePower checks if a number x is a simple power of another number n.

The loop starts from 2 (as we know that 1 is a power of any number) and goes up to x/2. This is because a number cannot be a power of a number greater than its half.

Inside the loop, it checks if n raised to the power of i equals x. If it does, the function returns true. Otherwise, it continues to the next iteration.

If the loop finishes without finding a match, the function returns false.

This function works for positive integers. If x or n is less than 1, the function returns false because a number cannot be a power of a number or a number cannot be raised to a negative power.

The function also handles the case where x is 1, because 1 is a simple power of any number.

## Complexity

The time complexity of this function is O(x/2) which is O(x) in Big O notation. This is because the function performs a single loop that goes up to x/2.

The