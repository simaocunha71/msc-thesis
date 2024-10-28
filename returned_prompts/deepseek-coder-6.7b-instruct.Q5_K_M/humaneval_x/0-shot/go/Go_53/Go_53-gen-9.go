
// 1. Convert x and y to float64
	xFloat64 := float64(x)
	yFloat64 := float64(y)

// 2. Add x and y
	result := xFloat64 + yFloat64

// 3. Convert the result back to int and return
	return int(result)
}

func main() {
	fmt.Println(Add(2, 3))
	fmt.Println(Add(5, 7))
}

*/

/*
Explanation:

In the function Add(), we first convert the parameters x and y from int to float64 to allow for decimal numbers. We then add these two numbers together. The result is then converted back to int and returned.

In the main() function, we test the Add() function with different pairs of numbers (2 and 3, 5 and 7) and print the results.
*/

/*
func Add(x int, y int) int {
	return x + y
}

func main() {
	fmt.Println(Add(2, 3))
	fmt.Println(Add(5, 7))
}
*/

/*
Explanation:

In the function Add(), we directly add the parameters x and y. The result is returned.

In the main() function, we test the Add() function with different pairs of numbers (2 and 3, 5 and 7) and print the results.
*/

/*
