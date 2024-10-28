
	note_lengths := []int{}
	notes := strings.Split(music_string, " ")

	for _, note := range notes {
		switch note {
		case "o":
			note_lengths = append(note_lengths, 4)
		case "o|":
			note_lengths = append(note_lengths, 2)
		case ".|":
			note_lengths = append(note_lengths, 1)
		default:
			continue
		}
	}

	return note_lengths
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```

In this code, the function `ParseMusic` takes a string `music_string` as an argument. This string is split into individual notes using the `strings.Split` function. 

A `switch` statement is used to check the type of each note. Depending on the note, the corresponding number of beats is appended to the `note_lengths` list.

Finally, the `note_lengths` list is returned as the result.

The `main` function calls `ParseMusic` with the string `"o o| .| o| o| .| .| .| .| o o"` and prints the result.

The output of this code will be `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`.

This is the expected output, as it represents the number of beats each note in the input string lasts.

This program is written in Go, a statically typed, compiled programming language designed at Google.

The time complexity of this program is O(n), where n is the number of notes in the input string, because we are iterating over the input string once. The space complexity is also O(n), because we are storing the length of each note in the `note_lengths` list.

## Code Explanation:

1. We import the necessary packages.
2. We define the function `ParseMusic` which takes a string `