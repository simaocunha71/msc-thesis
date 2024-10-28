
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

	var rev string
	for i := len(s) - 1; i >= 0; i-- {
		if 'a' <= s[i] && s[i] <= 'z' {
			rev += string(s[i] - 32)
		} else if 'A' <= s[i] && s[i] <= 'Z' {
			rev += string(s[i] + 32)
		} else {
			rev += string(s[i])
		}
	}
	return rev
}