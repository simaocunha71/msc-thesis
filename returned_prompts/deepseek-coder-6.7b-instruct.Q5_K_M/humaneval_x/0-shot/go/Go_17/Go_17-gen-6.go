
// Here is how to solve this problem:
// 1. Split the string by spaces to get a list of notes.
// 2. Initialize an empty list to store the lengths of the notes.
// 3. Loop over the list of notes.
// 4. For each note, check the type of note and add the corresponding length to the list.
// 5. Return the list of lengths.

B:

	notes := strings.Split(music_string," ")
	var lengths []int
	for _,note := range notes {
		switch note {
		case "o":
			lengths = append(lengths, 4)
		case "o|":
			lengths = append(lengths, 2)
		case ".|":
			lengths = append(lengths, 1)
		}
	}
	return lengths
}
```

## Code Explanation:

The code first splits the input string into a list of notes. This is done using the `strings.Split` function. The result is a list of strings, where each string represents a note.

Then, an empty list `lengths` is created. This will store the lengths of the notes in beats.

Next, a for loop is used to iterate over the list of notes. For each note, the type of note is checked using a switch statement. If the note is a whole note ('o'), it adds 4 to the list of lengths. If it's a half note ('o|'), it adds 2. If it's a quarter note ('.|'), it adds 1.

Finally, the list of lengths is returned.

The result of this code will be a list of integers representing the duration of each note in beats.

## Testing the function:

You can test the function by running the following code:

```go
func main() {
    fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```

This will output:

```go
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```