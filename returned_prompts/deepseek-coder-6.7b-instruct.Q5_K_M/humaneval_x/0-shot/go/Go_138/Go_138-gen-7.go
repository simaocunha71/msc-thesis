
// Create a counter to count the number of even numbers that can be summed up
evenCounter := 0

B:

// Iterate through all numbers from 2 up to n-1
for i := 2; i < n; i += 2 {

C:

// For each number, check if it can be summed up with the remaining numbers
for j := i + 2; j <= n; j += 2 {

D:

// If it can be summed up, increment the counter
evenCounter++
}
}

E:

// If the counter is 4, return true, else return false
return evenCounter == 4
}
*/

// IsEqualToSumEven checks if a given number n can be written as the sum of exactly 4 positive even numbers
func IsEqualToSumEven(n int) bool {
	if n < 8 || n%2 != 0 {
		return false
	}

	evenCounter := 0
	for i := 2; i <= n/2; i += 2 {
		if n-i > i {
			evenCounter++
		}
	}

	return evenCounter == 4
}

func main() {

	testCases := []struct {
		n        int
		expected bool
	}{
		{4, false},
		{6, false},
		{8, true},
		{10, false},
		{12, true},
		{14, false},
		{16, false},
		{18, true},
		{20, false},
		{22, false},
		{24, true},
	}

	for _, tc := range testCases {
		result := IsEqualToSumEven(tc.n)
		if result != tc.expected {
			fmt.Printf("For %d, expected %v but got %v\n", tc.n, tc.expected, result)
		}
	}
}

// This code is a simple test to check if a given number n can be written as the sum of exactly 4 positive even numbers.
// The function IsEqualToSumEven takes an integer n as input