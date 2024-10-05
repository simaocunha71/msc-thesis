    if len(numbers) == 0 {
        return []int{}
    }
    rollingMax := make([]int, len(numbers))
    rollingMax[0] = numbers[0]
    for i := 1; i < len(numbers); i++ {
        rollingMax[i] = int(math.Max(float64(rollingMax[i-1]), float64(numbers[i])))
    }
    return rollingMax
}
```

## Question 2

Write a Go program that returns the sum of all elements in a slice.

```go
package main

import (
	"fmt"
)

func SumSlice(numbers []int) int {
	sum := 0
	for _, num := range numbers {
		sum += num
	}
	return sum
}

func main() {
	numbers := []int{1, 2, 3, 4, 5}
	fmt.Println(SumSlice(numbers)) // Output: 15
}
```

## Question 3

Write a Go program that swaps two numbers without using a third variable.

```go
package main

import "fmt"

func swap(x, y int) (int, int) {
	x = x + y
	y = x - y
	x = x - y
	return x, y
}

func main() {
	x := 5
	y := 10
	fmt.Printf("Before swap: x = %d, y = %d\n", x, y)
	x, y = swap(x, y)
	fmt.Printf("After swap: x = %d, y = %d\n", x, y)
}
```

## Question 4

Write a Go program that calculates the factorial of a number using recursion.

```go
package main

import (
	"fmt"
)

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func main() {
	fmt.Println(factorial