for i, word := range strings.Split(sentence, " ") {
	if i == 0 {
		result += word
	} else {
		if !strings.Contains(result, word) {
			result += " " + word
		}
	}
}
return result
}

// 2.
// You are given a string,
// it contains some words separated by a space,
// and you have to return a string that contains the words from the original string,
// but each word should be repeated exactly 2 times,
// in the order they appear in the original string.
// 
// Example 1:
// Input: "hello world"
// Output: "hello world world"
// 
// Example 2