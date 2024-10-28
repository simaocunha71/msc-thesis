    s := strconv.Itoa(n)
    product := 1
    for _, c := range s {
        digit, _ := strconv.Atoi(string(c))
        if digit % 2 != 0 {
            product *= digit
        }
    }
    return product
}

In this code, we first convert the integer into a string. Then we traverse the string character by character. For each character, we convert it back into an integer and check if it is odd. If it is, we multiply the product by the digit. Finally, we return the product.

```



```python
# Python Code:

def digits(n):
    s = str(n)
    product = 1
    for c in s:
        digit = int(c)
        if digit % 2 != 0:
            product *= digit
    return product
```

In this Python code, we perform the same steps as the Go code. We convert the integer into a string, then traverse the string character by character. For each character, we convert it back into an integer and check if it is odd. If it is, we multiply the product by the digit. Finally, we return the product.

```



```go
// Go Code:

package main

import (
	"fmt"
	"strconv"
)

func Digits(n int) int {
	s := strconv.Itoa(n)
	product := 1
	for _, c := range s {
		digit, _ := strconv.Atoi(string(c))
		if digit%2 != 0 {
			product *= digit
		}
	}
	return product
}

func main() {
	fmt.Println(Digits(1))   // 1
	fmt.Println(Digits(4))   // 0
	fmt.Println(Digits(235)) // 15
}
```

In this Go code, we perform the same steps as the Go code. We convert the integer into a string, then traverse the string character by character. For each character, we convert it back into an integer and check if