import (
	"strconv"
	"strings"
)

// Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
// >>> FizzBuzz(50)
// 0
// >>> FizzBuzz(78)
// 2
// >>> FizzBuzz(79)
// 3
func FizzBuzz(n int) int {

}

Here is a possible solution in Go:

```go
func FizzBuzz(n int) int {
	count := 0
	for i := 1; i < n; i++ {
		if i%11 == 0 || i%13 == 0 {
			s := strconv.Itoa(i)
			for _, c := range s {
				if c == '7' {
					count++
				}
			}
		}
	}
	return count
}
```

This function works by iterating through all integers less than `n` and checking if they are divisible by 11 or 13. If they are, it converts the integer to a string and checks each character to see if it is '7'. If it is, the count is incremented. At the end, the function returns the count.
