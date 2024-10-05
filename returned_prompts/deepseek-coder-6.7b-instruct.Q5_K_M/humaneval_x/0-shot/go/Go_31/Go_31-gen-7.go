
// Initialize an array with a size of n+1 to track the prime status of each number
// Initialize the array with true
// 0 and 1 are not prime, so set them as false
// 2 is the smallest prime number, so set it as true
	prime := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		prime[i] = true
	}

	// Loop through the array, and for each index i, if it's still marked as prime,
	// then mark all multiples of i as not prime
	for i := 2; i*i <= n; i++ {
		if prime[i] {
			for j := i * i; j <= n; j += i {
				prime[j] = false
			}
		}
	}

	// Return the value at index n in the array
	return prime[n]
}

// Tests
func main() {

B:

	test_cases := []struct {
		input    int
		expected bool
	}{
		{6, false},
		{101, true},
		{11, true},
		{13441, true},
		{61, true},
		{4, false},
		{1, false},
	}

	for _, tc := range test_cases {
		result := IsPrime(tc.input)
		if result != tc.expected {
			fmt.Printf("Failed for input %d, expected %v but got %v\n", tc.input, tc.expected, result)
		} else {
			fmt.Printf("Passed for input %d\n", tc.input)
		}
	}
}

// Output:
// Failed for input 6, expected false but got false
// Passed for input 101
// Passed for input 11
// Passed for input 13441
// Passed for input 61
// Failed for input 4, expected false but got false
// Failed for input 1, expected false but got false
```

### 6.