    if len(strings) == 0 {
        return nil
    }

    longest := strings[0]
    for _, str := range strings {
        if len(str) > len(longest) {
            longest = str
        }
    }

    return longest
}
*/

// Longest returns the longest string in the slice
func Longest(strings []string) string {
	if len(strings) == 0 {
		return ""
	}

	longest := strings[0]
	for _, str := range strings {
		if len(str) > len(longest) {
			longest = str
		}
	}

	return longest
}

// Shortest returns the shortest string in the slice
func Shortest(strings []string) string {
	if len(strings) == 0 {
		return ""
	}

	shortest := strings[0]
	for _, str := range strings {
		if len(str) < len(shortest) {
			shortest = str
		}
	}

	return shortest
}

// FirstNonEmpty returns the first non-empty string in the slice
func FirstNonEmpty(strings []string) string {
	for _, str := range strings {
		if str != "" {
			return str
		}
	}

	return ""
}

// LastNonEmpty returns the last non-empty string in the slice
func LastNonEmpty(strings []string) string {
	for i := len(strings) - 1; i >= 0; i-- {
		if strings[i] != "" {
			return strings[i]
		}
	}

	return ""
}

// NonEmpty returns a slice of all non-empty strings in the input slice
func NonEmpty(strings []string) []string {
	nonEmptyStrings := make([]string, 0, len(strings))

	for _, str := range strings {
		if str != "" {
			nonEmptyStrings = append(nonEmptyStrings, str)
		}
	}

	return nonEmptyStrings
}

// Join joins all strings in the slice into one string with the specified separator
func Join(strings []