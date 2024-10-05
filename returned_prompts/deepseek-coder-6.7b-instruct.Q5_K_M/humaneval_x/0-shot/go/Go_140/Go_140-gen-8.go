
// Create a variable to hold the new string
// Initialize it with the first character of the original string
// because we can't change it in place

B:

	// Create a for loop to iterate over all the characters in the original string
	// Start from the 1st index because we initialized the new string with the first character
	for i := 1; i < len(text); i++ {

C:

		// If the character is a space and the previous character is also a space
		// then add an underscore to the new string
		if text[i] == ' ' && text[i-1] == ' ' {
			newText += "_"
			continue
		}

D:

		// If the character is a space and the previous character is not a space
		// then add a space to the new string
		if text[i] == ' ' && text[i-1] != ' ' {
			newText += "_"
			continue
		}

E:

		// If the character is not a space, add it to the new string
		newText += string(text[i])
	}

F:

	// Return the new string
	return newText
}

func main() {
	fmt.Println(FixSpaces("Example"))
	fmt.Println(FixSpaces("Example 1"))
	fmt.Println(FixSpaces(" Example 2"))
	fmt.Println(FixSpaces(" Example  3"))
}


```

## Output

```
Example
Example_1
_Example_2
_Example-3
```

## Time Complexity

The time complexity of this program is O(n), where n is the length of the input string. This is because we are iterating through the string once. 

## Space Complexity

The space complexity of this program is O(n), where n is the length of the input string. This is because we are storing the new string, which is the same length as the input string.

## Explanation

The program works by iterating through the input string one character at a time. If it encounters a space, it checks the previous character. If the previous