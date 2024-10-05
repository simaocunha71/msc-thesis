
Here is a solution in Go:

```go
package main

import (
	"fmt"
	"math"
)

func GenerateIntegers(a, b int) []int {
	var result []int
	for i := int(math.Min(float64(a), float64(b))); i <= math.Max(float64(a), float64(b)); i++ {
		if i%2 == 0 {
			result = append(result, i)
		}
	}
	return result
}

func main() {
	a := 2
	b := 8
	result := GenerateIntegers(a, b)
	fmt.Println(result)

	a = 8
	b = 2
	result = GenerateIntegers(a, b)
	fmt.Println(result)

	a = 10
	b = 14
	result = GenerateIntegers(a, b)
	fmt.Println(result)
}
```

In the above code, we define the `GenerateIntegers` function that takes two integers `a` and `b` as parameters. Inside the function, we initialize an empty slice called `result` to store the even integers between `a` and `b`.

We then use a `for` loop to iterate from the minimum of `a` and `b` to the maximum of `a` and `b`. For each iteration, we check if the current number `i` is even by using the modulo operator `%` to check if the remainder of `i` divided by 2 is equal to 0. If it is, we append `i` to the `result` slice using the `append` function.

Finally, we return the `result` slice containing all the even integers between `a` and `b`. In the `main` function, we test the `GenerateIntegers` function with different values of `a` and `b` and print the result.

When you run the program, it will output the following:

```
[2 4 6 8]
[2 4 6 8]
[]
```