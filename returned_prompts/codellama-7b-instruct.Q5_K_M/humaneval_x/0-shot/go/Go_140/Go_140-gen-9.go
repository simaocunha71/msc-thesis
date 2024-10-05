
// Given a string text, replace all spaces in it with underscores,
// and if a string has more than 2 consecutive spaces,
// then replace all consecutive spaces with -
// 
// FixSpaces("Example") == "Example"
// FixSpaces("Example 1") == "Example_1"
// FixSpaces(" Example 2") == "_Example_2"
// FixSpaces(" Example   3") == "_Example-3"
func FixSpaces(text string) string {
    var replacedText string
    var count int
    for _, char := range text {
        if char != ' ' {
            replacedText += string(char)
            count = 0
        } else {
            count++
            if count == 1 {
                replacedText += "_"
            } else if count >= 2 {
                replacedText += "-"
            }
        }
    }
    return replacedText
}
