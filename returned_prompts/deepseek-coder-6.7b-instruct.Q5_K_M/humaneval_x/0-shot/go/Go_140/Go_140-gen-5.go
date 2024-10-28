
	replace := func(c rune) rune {
		if c == ' ' {
			return '_'
		}
		return c
	}

	text = strings.Map(replace, text)

	replace2 := func(c rune) rune {
		if c == '-' {
			return '-'
		}
		return c
	}

	text = strings.Map(replace2, text)

	lastSpace := false
	return strings.Map(func(r rune) rune {
		if r == ' ' {
			if lastSpace {
				lastSpace = true
				return '-'
			} else {
				lastSpace = true
				return -1
			}
		} else {
			lastSpace = false
			return r
		}
	}, text)
}

// This function uses strings.Map to replace each character in the string with a new character determined by a function.
// The function takes a rune (a character) as input, and returns a new rune. If the function returns a space, the space is replaced with an underscore.
// Then, if a space is encountered, it is replaced with a hyphen if the last character was also a space, otherwise it is replaced with nothing (-1).
// Finally, the function returns the modified string.
```

The function `FixSpaces` is a solution to the problem. It takes a string as input and returns a string as output.
It replaces all spaces in the input string with underscores. If the string contains more than two consecutive spaces, it replaces all the consecutive spaces with a hyphen. If the string has less than two consecutive spaces, it leaves the string as it is.

The function `FixSpaces` uses the `strings.Map` function to replace each character in the string with a new character determined by a function. The function `replace` replaces all spaces with underscores, and the function `replace2` replaces all hyphens with nothing (-1).

Then, the function `FixSpaces` uses another `strings.Map` function to replace spaces with hyphens if the last character was also a space. The variable `lastSpace` is used to keep track of the last character.

Finally, the function `Fix