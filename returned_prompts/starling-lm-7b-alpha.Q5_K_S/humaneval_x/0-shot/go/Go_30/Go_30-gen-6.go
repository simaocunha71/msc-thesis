
```go
func GetPositive(l []int) []int {
	positive := []int{}
	for _, v := range l {
		if v > 0 {
			positive = append(positive, v)
		}
	}
	return positive
}
```

Here's how the code works:

1. We start by defining a function called `GetPositive` that takes in a slice of integers (`l`) and returns a slice of integers.
2. Inside the function, we create an empty slice called `positive` to store the positive numbers.
3. We use a `for` loop to iterate over each element in the input slice `l`. For each element, we check if it's greater than zero using the condition `v > 0`. If it is, we append it to the `positive` slice using the `append()` function.
4. After iterating through all the elements in the input slice, we return the `positive` slice which contains only the positive numbers.
5. This function can be tested using the provided test cases. For example, `GetPositive([-1, 2, -4, 5, 6])` should return `[2, 5, 6]` and `GetPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])` should return `[5, 3, 2, 3, 9, 123, 1]`.

This implementation efficiently filters out the negative numbers from the input slice and returns only the positive numbers, providing a clear and concise solution to the problem.

```go
package main

func main() {
	print(GetPositive([]int{-1, 2, -4, 5, 6})) // [2, 5, 6]
	print(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // [5, 3, 2, 3, 9, 123, 1]
}
``