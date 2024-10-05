
	music := []rune(music_string)
	beats := make([]int, 0)
	
	for i := 0; i < len(music); i++ {
		switch music[i] {
		case 'o':
			if i+1 < len(music) && music[i+1] == '|' {
				beats = append(beats, 2)
				i++
			} else {
				beats = append(beats, 4)
			}
		case '.':
			if i+1 < len(music) && music[i+1] == '|' {
				beats = append(beats, 1)
				i++
			}
		}
	}
	
	return beats
}
```

The function ParseMusic takes as input a string music_string and returns a list of integers representing the number of beats each note in the music_string lasts. It does this by iterating over the string, and for each character in the string, it checks if it is an 'o', a '.' or a '|' and depending on the character and the next character, it appends the corresponding number of beats to the list beats.

For example, if the input string is "o o| .| o| o| .| .| .| .| o o", the function will return the list [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4].

This function is case sensitive, so it will not work correctly if the input string contains uppercase letters.

Note: This function assumes that the input string is a valid music string as per the given format. If there are any invalid characters in the string, the function may not work as expected.

Also, the function does not handle the case where the input string contains uppercase letters. If you need to handle that case, you would need to add additional code to convert uppercase letters to lowercase or handle them differently.

If you need to handle more complex cases, such as different note types that last different lengths of time, you would need to modify the function to handle those cases.

The function uses