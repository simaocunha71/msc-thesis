
// You are given a string s.
// if s[i] is a letter, reverse its case from lower to upper or vise versa,
// otherwise keep it as it is.
// If the string contains no letters, reverse the string.
// The function should return the resulted string.
// Examples
// Solve("1234") = "4321"
// Solve("ab") = "AB"
// Solve("#a@C") = "#A@c"
func Solve(s string) string {
    if strings.ContainsAny(s, []rune{}) == false && len([]rune(s)) > 0 { // if the string contains numbers or chars and is not empty then reverse it
        return Reverse(s);
    } else {
        return s; // otherwise keep as is
    }
}
