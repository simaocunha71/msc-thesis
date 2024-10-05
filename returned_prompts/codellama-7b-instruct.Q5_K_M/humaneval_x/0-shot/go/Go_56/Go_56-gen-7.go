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

	var stack []string

	for _, bracket := range brackets {
		switch bracket {
		case '<':
			stack = append(stack, ">")
		case '>':
			if len(stack) == 0 || stack[len(stack)-1] != ">" {
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
