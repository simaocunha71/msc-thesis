
	max := l[0]
	for _, value := range l {
		if value > max {
			max = value
		}
	}
	return max
}




```

## Exercise 2

Write a function in Go that takes a slice of integers and returns the sum of the squares of the elements in the slice.

```go
package main

import "fmt"

func sumOfSquares(numbers []int) int {

	// your code here

}

func main() {
	numbers := []int{1, 2, 3, 4, 5}
	fmt.Println(sumOfSquares(numbers)) // Output: 55
}

```

## Answer 2

```go
package main

import "fmt"

func sumOfSquares(numbers []int) int {
	sum := 0
	for _, num := range numbers {
		sum += num * num
	}
	return sum
}

func main() {
	numbers := []int{1, 2, 3, 4, 5}
	fmt.Println(sumOfSquares(numbers)) // Output: 55
}

```

## Exercise 3

Write a Go program that declares a variable of type string, initializes it with your name, and prints it.

```go

```

## Answer 3

```go
package main

import "fmt"

func main() {
	var name string = "John Doe"
	fmt.Println(name)
}

```

## Exercise 4

Write a Go program that declares a variable of type int, initializes it with your age, and prints it.

```go

```

## Answer 4

```go
package main

import "fmt"

func main() {
	var age int = 30
	fmt.Println(age)
}

```

## Exercise 5

Write a Go program that declares a variable of type bool and initializes it to true or false, and prints it.