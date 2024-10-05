
```go
package main

import (
	"fmt"
	"strconv"
)

func CircularShift(x int, shift int) string {
	str := fmt.Sprint(x)
	lenStr := len(str)
	if shift > lenStr {
		shift = shift % lenStr
	}
	shiftStr := str[lenStr-shift:] + str[:lenStr-shift]
	i, _ := strconv.Atoi(shiftStr)
	return fmt.Sprint(i)
}
```

Explanation:
This function first converts the integer to a string using fmt.Sprint(). Then it calculates the length of the string. If the shift is larger than the length of the string, it reduces the shift to the modulus of the length of the string. This is to ensure that the shift is within the range of the string length. The function then takes a substring of the string starting from the index lenStr-shift till the end and concatenates it with the substring from the beginning till lenStr-shift-1. This effectively shifts the digits of the string to the right by shift positions. The shifted string is then converted back to an integer using strconv.Atoi() and returned as a string using fmt.Sprint().

The function can be tested with the following code:

```go
package main

import "fmt"

func main() {
	fmt.Println(CircularShift(12, 1)) // "21"
	fmt.Println(CircularShift(12, 2)) // "12"
}
```

This will output:

```
21
12
```

This means that the function is correctly shifting the digits of the integer to the right by the specified shift value and returning the result as a string.

```go
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