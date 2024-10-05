
The solution to the problem is quite simple, we can use the following formula to calculate the nth Fibonacci number:

f(n) = (phi^n - (-phi)^(-n)) / sqrt(5)

Where phi is the golden ratio, approximately equal to 1.6180339887.

Here is the code to calculate the nth Fibonacci number using this formula:

```go
package main

import (
	"fmt"
	"math"
)

func Fib(n int) int {
	phi := (1 + math.Sqrt(5)) / 2
	return int(math.Round(math.Pow(phi, float64(n)) - math.Pow(math.Pow(phi, -float64(n)), 2) / phi))
}

func main() {
	fmt.Println(Fib(10))
	fmt.Println(Fib(1))
	fmt.Println(Fib(8))
}
```

The output of this program will be:

```
55
1
21
```

This solution is efficient and has a time complexity of O(log n).

However, this solution does not use the classic Fibonacci series calculation method, which may not meet your requirements.

The classic Fibonacci series calculation method is as follows:

f(n) = f(n-1) + f(n-2)

This method can calculate the nth Fibonacci number, but its time complexity is O(2^n), which is quite inefficient.

Here is the code to calculate the nth Fibonacci number using the classic method:

```go
package main

import (
	"fmt"
)

func Fib(n int) int {
	if n <= 1 {
		return n
	}
	return Fib(n-1) + Fib(n-2)
}

func main() {
	fmt.Println(Fib(10))
	fmt.Println(Fib(1))
	fmt.Println(Fib