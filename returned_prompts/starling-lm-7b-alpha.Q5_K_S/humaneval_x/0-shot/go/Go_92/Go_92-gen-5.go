
func AnyInt(x, y, z interface{}) bool {
    // Check if all numbers are integers
    if !isInteger(x) || !isInteger(y) || !isInteger(z) {
        return false
    }
    // Check if one of the numbers is equal to the sum of the other two
    return (x + y == z) || (y + z == x) || (x + z == y)
}

func isInteger(i interface{}) bool {
    _, ok := i.(int)
    return ok
}































```

```

```

```go
package main

import (
	"fmt"
)

func AnyInt(x, y, z interface{}) bool {
	// Check if all numbers are integers
	if !isInteger(x) || !isInteger(y) || !isInteger(z) {
		return false
	}
	// Check if one of the numbers is equal to the sum of the other two
	return (x + y == z) || (y + z == x) || (x + z == y)
}

func isInteger(i interface{}) bool {
	_, ok := i.(int)
	return ok
}

func main() {
	fmt.Println(AnyInt(5, 2, 7))
	fmt.Println(AnyInt(3, 2, 2))
	fmt.Println(AnyInt(3, -2, 1))
	fmt.Println(AnyInt(3.6, -2.2, 2))
}
```
```

```

```go
package main

import (
	"fmt"
)

func AnyInt(x, y, z interface{}) bool {
	// Check if all numbers are integers
	if !isInteger(x) || !isInteger(y) || !isInteger(z) {
		return false
	}
	// Check if one of the numbers is equal to the sum of the other two
	return (x + y