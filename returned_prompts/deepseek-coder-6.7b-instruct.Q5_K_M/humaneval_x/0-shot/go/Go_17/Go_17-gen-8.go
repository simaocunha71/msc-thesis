
    var notes []int
    note_strings := strings.Split(music_string, " ")

    for _, note_string := range note_strings {
        switch note_string {
        case "o":
            notes = append(notes, 4)
        case "o|":
            notes = append(notes, 2)
        case ".|":
            notes = append(notes, 1)
        }
    }

    return notes
}
```

The function takes a string of music notes and splits it by spaces. For each note, it checks the special ASCII characters to determine how long it lasts (whole note = 4 beats, half note = 2 beats, quater note = 1 beat) and adds the duration to the notes list. Finally, it returns the list of note durations.

## Test Cases

```go
fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o")) // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
fmt.Println(ParseMusic("o| o| o| o|")) // [2, 2, 2, 2]
fmt.Println(ParseMusic("o .| o| .|")) // [4, 1, 2, 1, 1]
```

## Discussion

This problem is about string parsing and ASCII character recognition. We split the string by spaces to get individual notes. Then we check each note to determine how long it lasts and add that duration to our notes list. Finally, we return the list of note durations.

## Note

This problem is relatively easy, but understanding the ASCII representation of the notes is key. The solution provided assumes that the input string will always be in the correct format. If this is not the case, we would need to add error handling to account for invalid input.

## Time Complexity

The time complexity of this solution is O(n), where n is the number of notes in the input string. This is because we are iterating over the input string once.

## Space Complexity

The space complexity