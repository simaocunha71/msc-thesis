
func SumProduct(numbers []int) (sum, product int) {
	sum = 0
	product = 1
	for _, n := range numbers {
		sum += n
		product *= n
	}
	return
}

The SumProduct function takes a slice of integers as an argument and returns a tuple of two integers: the sum of all the integers in the slice, and the product of all the integers in the slice. If the slice is empty, the function returns the tuple (0, 1), which represents an empty sum and an empty product.

To calculate the sum, the function initializes a variable called `sum` to 0. Then, it iterates over each element `n` in the `numbers` slice using a range loop. For each element, it adds `n` to the `sum` variable. After the loop, the function returns the calculated sum.

To calculate the product, the function initializes a variable called `product` to 1. Then, it iterates over each element `n` in the `numbers` slice using a range loop. For each element, it multiplies `n` with the current value of `product` and assigns the result back to the `product` variable. After the loop, the function returns the calculated product.

By returning the `sum` and `product` variables directly as the result of the function, we can use them as the values of the tuple returned by the function.

Here's an example usage of the SumProduct function:

numbers := []int{1, 2, 3, 4}
sum, product := SumProduct(numbers)
fmt.Println(sum, product) // Output: 10, 24

In this example, we pass a slice of integers `[1, 2, 3, 4]` to the SumProduct function. The function calculates the sum of the integers as 10 and the product as 24. The result is printed to the console as (10, 24).

The SumProduct function demonstrates a common pattern in Go called "multi-value return". Instead of returning a single value, the function returns multiple values as a tuple. This allows us to return multiple pieces of information from a function in a single call