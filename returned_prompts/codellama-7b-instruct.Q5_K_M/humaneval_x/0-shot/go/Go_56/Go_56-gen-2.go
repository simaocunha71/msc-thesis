
// brackets is a string of "<" and ">".
// return true if every opening bracket has a corresponding closing bracket.
// 
// >>> CorrectBracketing("<")
// false
// >>> CorrectBracketing("<>")
// true
// >>> CorrectBracketing("<<><>>")
// true
// >>> CorrectBracketing("><<>")
// false
func CorrectBracketing(brackets string) bool {
	var stack []rune
	for _, r := range brackets {
		switch r {
		case '<':
			stack = append(stack, r)
		case '>':
			if len(stack) == 0 {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}

func main() {
	fmt.Println(CorrectBracketing("<"))
	fmt.Println(CorrectBracketing("<>"))
	fmt.Println(CorrectBracketing("<<><>>"))
	fmt.Println(CorrectBracketing("><<>"))
}
