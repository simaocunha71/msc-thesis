
	// Convert to slices of runes
	r0 := []rune(s0)
	r1 := []rune(s1)

	// Sort both slices
	sort.Slice(r0, func(i, j int) bool { return r0[i] < r0[j] })
	sort.Slice(r1, func(i, j int) bool { return r1[i] < r1[j] })

	// Compare slices
	return reflect.DeepEqual(r0, r1)
}

func main() {

	tests := []struct{ s0, s1 string; want bool }{
		{"eabcdzzzz", "dddzzzzzzzddeddabc", true},
		{"abcd", "dddddddabc", true},
		{"dddddddabc", "abcd", true},
		{"eabcd", "dddddddabc", false},
		{"abcd", "dddddddabce", false},
		{"eabcdzzzz", "dddzzzzzzzddddabc", false},
	}

	for _, test := range tests {
		got := SameChars(test.s0, test.s1)
		if got != test.want {
			fmt.Printf("SameChars(%q, %q) = %v; want %v\n", test.s0, test.s1, got, test.want)
		}
	}
}
```

This program first converts the strings to slices of runes. Then it sorts these slices. Finally, it checks if the sorted slices are equal. If they are, the function `SameChars` returns true. Otherwise, it returns false.

The program then runs a series of tests on the `SameChars` function and prints out any test cases that failed.

The time complexity of this solution is O(n log n), where n is the length of the string. This is due to the sorting of the rune slices. The space complexity is also O(n), due to the creation of the rune slices.

Note: The `SameChars` function assumes that the input strings are in ASC