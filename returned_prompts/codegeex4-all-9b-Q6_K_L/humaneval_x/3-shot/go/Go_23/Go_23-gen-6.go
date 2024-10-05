
Your A: for the first question is correct. The second question is also correct. The third question can be improved by using the built-in "strconv" package to convert the number to a string and then get the length of the string. Here is the improved version of your code:

// Return length of given number
// >>> Strlen(3.5)
// 1
func Strlen(number float64) int {
    return len(strconv.FormatFloat(number, 'f', -1, 64))
}