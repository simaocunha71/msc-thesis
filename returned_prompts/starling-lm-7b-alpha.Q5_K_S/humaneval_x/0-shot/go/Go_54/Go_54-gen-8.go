
// Sort both strings
s0 = strings.Map(func(r rune) rune { return toLower(r) }, s0)
s1 = strings.Map(func(r rune) rune { return toLower(r) }, s1)
s0 = strings.ToLower(s0)
s1 = strings.ToLower(s1)

s0 = strings.Join(sortString(s0), "")
s1 = strings.Join(sortString(s1), "")

if s0 == s1 {
	return true
} else {
	return false
}
}

func toLower(r rune) rune {
if 'A' <= r && r <= 'Z' {
return r - 'A' + 'a'
}
return r
}

func sortString(s string) []string {
runes := []rune(s)
sort.Slice(runes, func(i, j int) bool {
return runes[i] < runes[j]
})
return string(runes)
}


In the solution, we first convert the strings to lowercase to ensure case-insensitive comparison. Then, we sort the characters in each string using the `sortString` function. Finally, we compare the sorted strings to determine if they have the same characters.

The `toLower` function is used to convert uppercase letters to lowercase. It takes a rune as input and returns the lowercase version of the rune if it is an uppercase letter, otherwise, it returns the rune as is.

The `sortString` function takes a string as input and returns a slice of strings with the characters sorted in ascending order. It uses the `sort.Slice` function to sort the runes in the string.

Overall, the solution ensures that the input strings are compared in a case-insensitive manner and in the same order, allowing for accurate determination of whether the strings have the same characters.

In the provided test cases, the `SameChars` function is called with different input strings to demonstrate its functionality. The expected outputs are also provided to verify the correctness of the solution.

Note that the `SameChars` function is exported and can be used in other packages.

// Check if two