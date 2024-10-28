
// Given a string text, replace all spaces in it with underscores,
// and if a string has more than 2 consecutive spaces,
// then replace all consecutive spaces with -
// 
// FixSpaces("Example") == "Example"
// FixSpaces("Example 1") == "Example_1"
// FixSpaces(" Example 2") == "_Example_2"
// FixSpaces(" Example   3") == "_Example-3"
func FixSpaces(text string) string {
	var result string
	for i, r := range text {
		if r == ' ' {
			if i > 0 && text[i-1] == ' ' {
				result += "-"
			}
			result += "_"
		} else {
			result += string(r)
		}
	}
	return result
}