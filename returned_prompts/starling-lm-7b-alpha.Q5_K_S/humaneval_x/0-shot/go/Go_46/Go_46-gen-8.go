
```go
package main

import "fmt"

func Fib4(n int) int {
	a, b, c, d := 0, 0, 2, 0
	for i := 2; i <= n; i++ {
		if i%4 == 0 {
			d = a + b + c + d
		} else if i%4 == 1 {
			d = a + c
		} else if i%4 == 2 {
			d = b + c
		} else if i%4 == 3 {
			d = a + b
		}
		a, b, c, d = b, c, d, d
	}
	return d
}

func main() {
	fmt.Println(Fib4(5)) // 4
	fmt.Println(Fib4(6)) // 8
	fmt.Println(Fib4(7)) // 14
}
```

The Fib4 number sequence can be computed by using a loop and a few variables to store the last four Fib4 numbers. We iterate from 2 to n, and for each iteration, we calculate the next Fib4 number based on the current position modulo 4. The result is stored in d, and the variables a, b, c, and d are updated accordingly. Finally, the function returns the n-th Fib4 number.

The time complexity of this solution is O(n) since we need to iterate through all the numbers from 2 to n.

In the main function, we test the Fib4 function with the provided test cases and print the results.

```go
package main

import "fmt"

func Fib4(n int) int {
	a, b, c, d := 0, 0, 2, 0
	for i := 2; i <= n; i++ {
		if i%4 == 0 {
			d = a + b + c + d
		} else if i%4 == 1 {
			d = a + c
		} else if i%4 == 2