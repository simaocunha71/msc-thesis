
    // Create a stack to store the brackets.
    stack := []rune{}

    // Iterate over the string.
    for _, c := range s {

B:

        // If the character is an opening bracket, push it to the stack.
        if c == '[' {
            stack = append(stack, c)
            continue
        }

C:

        // If the character is a closing bracket.
        // If the stack is empty, return false.
        // Otherwise, pop the top element from the stack.
        if len(stack) == 0 {
            return false
        }
        stack = stack[:len(stack)-1]
    }

    // If the stack is not empty, return true. Otherwise, return false.
    return len(stack) != 0
}

func main() {

    fmt.Println(IsNested("[[]]"))         // ➞ true
    fmt.Println(IsNested("[]]]]]]][[[[[]")) // ➞ false
    fmt.Println(IsNested("[][]"))         // ➞ false
    fmt.Println(IsNested("[]"))           // ➞ false
    fmt.Println(IsNested("[[][]]"))       // ➞ true
    fmt.Println(IsNested("[[]][["))       // ➞ true
}

*/

// IsNested checks if there is a valid subsequence of brackets where at least one bracket in the subsequence is nested.
func IsNested(s string) bool {
	stack := []rune{}
	for _, c := range s {
		if c == '[' {
			stack = append(stack, c)
		} else if len(stack) == 0 || stack[len(stack)-1] != '[' {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) != 0
}

// TestIsNested tests the IsNested function.
func TestIsNested(t *testing.T) {
	t.