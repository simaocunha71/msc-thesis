
// We'll use a simple loop to iterate through each string in the list
// and check if it starts with the given prefix.
// If it does, we'll append it to the output list.

var output []string

for _, str := range strings {
    if strings.HasPrefix(str, prefix) {
        output = append(output, str)
    }
}

return output
}

// This function works by looping through each string in the input list
// and checking if it starts with the given prefix using the strings.HasPrefix function.
// If the string does start with the prefix, it is added to the output list.
// The output list is then returned.

// This function has a time complexity of O(n) because it makes a single pass over the input list,
// where n is the length of the input list. The space complexity is also O(n) because in the worst case,
// where all strings in the input list start with the given prefix, we might end up appending all of them to the output list.

*/

func FilterByPrefix(strings []string, prefix string) []string {
	var output []string
	for _, str := range strings {
		if strings.HasPrefix(str, prefix) {
			output = append(output, str)
		}
	}
	return output
}

// ------------------

// 1.2.5

/*

