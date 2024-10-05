
    // Base case when n is less than 2
    if n < 2 {
        return []int{}
    }

    // Initialize a slice with the first prime number
    primes := []int{2}

    // Iterate over all the numbers from 3 to n
    for i := 3; i < n; i += 2 {
        isPrime := true

        // Check if the current number is a prime
        for _, prime := range primes {
            if prime*prime > i {
                break
            }
            if i%prime == 0 {
                isPrime = false
                break
            }
        }

        // If the number is prime, append it to the list
        if isPrime {
            primes = append(primes, i)
        }
    }

    return primes
}

```

## Solution to problem 2

```go
package main

import (
	"fmt"
	"strings"
)

func StringMask(s string, f func(rune) bool) string {
	var result strings.Builder
	for _, char := range s {
		if f(char) {
			result.WriteRune(char)
		} else {
			result.WriteRune('*')
		}
	}
	return result.String()
}

func main() {
	msg := "Hello, World!"
	filter := func(r rune) bool {
		return r != 'o' && r != 'l'
	}
	fmt.Println(StringMask(msg, filter))
}

```

## Solution to problem 3

```go
package main

import (
	"fmt"
)

func main() {
	str := "Hello, World!"
	reverseStr := ""

	for _, value := range str {
		reverseStr = string(value) + reverseStr
	}

	fmt.Println(reverseStr)
}
```

## Solution to problem 4

```go
package main

import (
	"fmt"
	"strings"
)

func main