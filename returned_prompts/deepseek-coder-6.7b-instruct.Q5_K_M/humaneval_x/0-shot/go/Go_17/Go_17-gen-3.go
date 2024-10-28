
	beat_values := []int{}
	notes := strings.Split(music_string, " ")

	for _, note := range notes {
		switch note {
		case "o":
			beat_values = append(beat_values, 4)
		case "o|":
			beat_values = append(beat_values, 2)
		case ".|":
			beat_values = append(beat_values, 1)
		}
	}

	return beat_values
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```

This function works by first splitting the input string into a slice of strings, each representing a note. It then loops over each note in the slice, and appends the corresponding number of beats to the `beat_values` slice. Finally, it returns this slice.

This function assumes that the input string will always be correctly formatted. If the input string could have errors, the function would need to be modified to handle these cases.

The function also assumes that the input string will always contain only the characters 'o', 'o|', and '.|', as specified in the problem statement. If the input string could contain other characters, the function would need to be modified to handle these cases.

The time complexity of this function is O(n), where n is the number of notes in the input string. This is because the function loops over each note in the input string once. The space complexity is also O(n), because the function creates a new slice to hold the beat values.

This function is a good example of how to use the `strings.Split` function in Go, which splits a string into a slice of substrings based on a specified separator. It's also a good example of how to use the `append` function, which adds an element to the end of a slice.

In summary, this function is a simple and efficient way to parse a string representing musical notes into a list of integers representing how many beats each note lasts.



```go

```




























