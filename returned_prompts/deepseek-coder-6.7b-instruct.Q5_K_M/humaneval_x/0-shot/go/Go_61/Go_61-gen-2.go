    count := 0
    for _, b := range brackets {
        if b == '(' {
            count++
        } else if b == ')' && count > 0 {
            count--
        } else {
            return false
        }
    }

    return count == 0
}

*/

// CorrectBracketing is a function to check if every opening bracket has a corresponding closing bracket.
func CorrectBracketing(brackets string) bool {
	stack := []rune{}
	for _, b := range brackets {
		switch b {
		case '(':
			stack = append(stack, b) // push
		case ')':
			if len(stack) == 0 {
				return false
			}
			stack = stack[:len(stack)-1] // pop
		}
	}
	return len(stack) == 0
}

func main() {
	fmt.Println(CorrectBracketing("("))         // false
	fmt.Println(CorrectBracketing("()"))        // true
	fmt.Println(CorrectBracketing("(()())"))    // true
	fmt.Println(CorrectBracketing(")(()"))      // false
	fmt.Println(CorrectBracketing(")("))        // false
	fmt.Println(CorrectBracketing("())(()"))    // false
	fmt.Println