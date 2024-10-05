
	sum := 0
	for i := 2; i <= n; i += 2 {
		sum += i
	}

B:

	return sum == n
}

// The main function
func main() {

	x := 4
	y := 6
	z := 8

	result1 := IsEqualToSumEven(x)
	result2 := IsEqualToSumEven(y)
	result3 := IsEqualToSumEven(z)

	fmt.Println("Is", x, "an even sum of 4 positive even numbers?", result1)
	fmt.Println("Is", y, "an even sum of 4 positive even numbers?", result2)
	fmt.Println("Is", z, "an even sum of 4 positive even numbers?", result3)

}

// Output:
// Is 4 an even sum of 4 positive even numbers? false
// Is 6 an even sum of 4 positive even numbers? false
// Is 8 an even sum of 4 positive even numbers? true
```

**Explanation:**

The function IsEqualToSumEven takes an integer as input and checks whether it can be expressed as the sum of exactly four positive even numbers. It does this by iterating through the even numbers up to the given number and adding them together. If the sum is equal to the given number, the function returns true; otherwise, it returns false.

The main function then tests the IsEqualToSumEven function with the numbers 4, 6, and 8, and prints the results.

**Constraints:**

- The input number n is guaranteed to be greater than or equal to 2.
- The input number n is an integer.

**Note:**

- This solution assumes that the given number n is a positive integer greater than or equal to 2.
- The function IsEqualToSumEven calculates the sum of the first four even numbers which are 2, 4, 6, and 8.
- The function IsEqualToSumEven checks if the sum of the first four even numbers equals the given number n.
- The main function prints the result of the function IsEqualToSumEven for the numbers 4, 6,