
	// Count the character frequency in s0
	counts0 := make(map[rune]int)
	for _, char := range s0 {
		counts0[char]++
	}

B:

	// Check if character frequency in s1 is the same
	for _, char := range s1 {
		if counts0[char] == 0 {
			return false
		}
		counts0[char]--
	}

	// Check if all counts in counts0 are 0
	for _, count := range counts0 {
		if count != 0 {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc")) // true
	fmt.Println(SameChars("abcd", "dddddddabc"))             // true
	fmt.Println(SameChars("dddddddabc", "abcd"))             // true
	fmt.Println(SameChars("eabcd", "dddddddabc"))             // false
	fmt.Println(SameChars("abcd", "dddddddabce"))             // false
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc")) // false
}

```

This code implements the function `SameChars` that checks if two strings have the same characters. It first counts the occurrence of each character in the first string (`s0`). It then checks if the same characters occur in the second string (`s1`) with the same frequencies. If all characters occur with the same frequency in `s1`, the function returns `true`; otherwise, it returns `false`.

This implementation is case sensitive and handles strings with Unicode characters.

The time complexity of this function is O(n), where n is the length of the longer string. The space complexity is also O(n), as we store the count of each character in a map.

Note: The order of characters in the strings does not matter for the result to be true.

This function is case sensitive and handles Unicode characters.

```

```
