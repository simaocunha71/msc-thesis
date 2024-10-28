
	stk := []rune{}

	for _, ch := range s {
		if ch == '[' {
			stk = append(stk, ch)
		} else if ch == ']' && len(stk) > 0 {
			if stk[len(stk)-1] == '[' {
				return true
			}
			stk = stk[:len(stk)-1]
		}
	}
	return false
}

// Main Function
func main() {
	fmt.Println(IsNested("[[]]")) //➞ true
	fmt.Println(IsNested("[]]]]]]][[[[[]")) //➞ false
	fmt.Println(IsNested("[][]")) //➞ false
	fmt.Println(IsNested("[]")) //➞ false
	fmt.Println(IsNested("[[][]]")) //➞ true
	fmt.Println(IsNested("[[]][[")) //➞ true
}

// Explanation:
// In the first test case, there are two valid subsequences: "[]" and "[[]]". 
// Both are nested, so the function returns true.
// 
// In the second test case, there are no valid subsequences. The function returns false.
// 
// In the remaining test cases, there are no valid subsequences of brackets that are nested. 
// Thus, the function returns false.
// 
// The function works by iterating over the input string and using a stack to keep track of open brackets. 
// When it encounters a closed bracket, it checks if the last element in the stack is an open bracket. 
// If so, it returns true because a valid subsequence of brackets has been found. 
// If not, it removes the last element from the stack and continues. 
// If it finishes iterating over the string without finding a valid subsequence of brackets that are nested, it returns false.
// 
// This function assumes that the input string only contains square brackets and that it is non-empty. 
// If this is not the case, additional error checking should be added.
// 
