// You can use the unicode package to get the character code for a character and compare it to the codes for "<" and ">". 
// The code for "<" is 60 (0x3c) and the code for ">" is 62 (0x3e).
// You can iterate over the string and check if each character is an opening bracket or a closing bracket.
// If it is an opening bracket, you can increment a counter.
// If it is a closing bracket, you can decrement the counter.
// If the counter is negative, then there are more closing brackets than opening brackets.
// If the counter is not zero after iterating over the string, then there are more opening brackets than closing brackets.
// If the counter is zero after iterating over the string, then there are the same number of opening and closing brackets.
// You can return true if the counter is zero, and false otherwise.
func CorrectBracketing(brackets string) bool {
    count := 0
    for _, c := range brackets {
        if c == '<' {
            count++
        } else if c == '>' {
            count--
        }
        if count < 0 {
            return false
        }
    }
    return count == 0
}