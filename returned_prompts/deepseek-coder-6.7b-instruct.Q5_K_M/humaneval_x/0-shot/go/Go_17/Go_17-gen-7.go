
	result := make([]int, 0)
	notes := strings.Split(music_string, " ")

	for _, note := range notes {

		switch note {
		case "o":
			result = append(result, 4)
		case "o|":
			result = append(result, 2)
		case ".|":
			result = append(result, 1)
		}
	}

	return result
}
```

## Code Explanation

This function ParseMusic takes a string `music_string` as input. This string is split into individual notes by using the `strings.Split` function.

A `for` loop is used to iterate over each note. A `switch` statement is used to determine how many beats each note lasts. The length of each note is determined by the number of characters in the string representation of the note.

The length of each note is then appended to the `result` slice. This slice is returned at the end of the function.

The function uses the `append` function to add the length of each note to the `result` slice. The `append` function returns a new slice containing all the elements of the original slice followed by the new elements. In this case, it's used to add the length of each note to the `result` slice.

The `result` slice is initialized as an empty slice of integers. The `append` function is used to add the length of each note to the `result` slice. The `result` slice is then returned as the output of the function.

The time complexity of the function is O(n), where n is the number of notes in the input string. The space complexity is also O(n), as a new slice is created to store the lengths of the notes.

## Test Cases

Here are some test cases for the function:

```go
fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))  // should return [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
fmt.Println(ParseMusic("o| o| o