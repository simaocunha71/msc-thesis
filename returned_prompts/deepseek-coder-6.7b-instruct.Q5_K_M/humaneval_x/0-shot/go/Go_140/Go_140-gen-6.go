
}

*/

func FixSpaces(text string) string {

	result := ""
	count := 0

	for _, char := range text {

		if string(char) == " " {
			count++
		} else {
			if count > 2 {
				result += "-"
			} else if count > 0 {
				result += "_"
			}
			result += string(char)
			count = 0
		}
	}

	if count > 2 {
		result = strings.Replace(result, " ", "-", -1)
	} else if count > 0 {
		result = strings.Replace(result, " ", "_", -1)
	}

	return result
}

func main() {
	fmt.Println(FixSpaces("Example"))       // "Example"
	fmt.Println(FixSpaces("Example 1"))     // "Example_1"
	fmt.Println(FixSpaces(" Example 2"))    // "_Example_2"
	fmt.Println(FixSpaces(" Example  3"))   // "_Example-3"
	fmt.Println(FixSpaces("Example   1 2")) // "Example-1-2"
}


/*
In this problem, we are asked to replace all spaces in the given string with underscores,
except for the case when there are more than two consecutive spaces,
in which case we replace those with hyphens.

We can solve this problem by iterating through each character of the string and keeping track of how many consecutive spaces we've encountered.
When we encounter a non-space character, we add the appropriate number of underscores or hyphens to our result string, and then add the non-space character itself.

Finally, if there are more than two consecutive spaces left in the text, we replace all spaces in our result string with hyphens, otherwise we replace them with underscores.
*/


/*
func FixSpaces(text string) string {
	res := ""
	spaceCount := 0
	for _, c := range text {
		if c == ' ' {
			spaceCount++
		} else {
			if spaceCount > 2 {
