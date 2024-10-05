
	stack := []rune{}
	for _, c := range s {
		if c == '[' {
			stack = append(stack, c)
		} else if c == ']' {
			if len(stack) == 0 || stack[len(stack)-1] != '[' {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) != 0
}

func main() {
	fmt.Println(IsNested("[[]]")) // ➞ true
	fmt.Println(IsNested("[]]]]]]][[[[[]")) // ➞ false
	fmt.Println(IsNested("[][]")) // ➞ false
	fmt.Println(IsNested("[]")) // ➞ false
	fmt.Println(IsNested("[[][]]")) // ➞ true
	fmt.Println(IsNested("[[]][[")) // ➞ true
}

// Explanation:
// In the first example, there are two valid subsequences of brackets: "[[]]" and "[][]". Both have at least one nested bracket.
// In the second example, there are no valid subsequences of brackets.
// In the third example, there are no valid subsequences of brackets.
// In the fourth example, there are no valid subsequences of brackets.
// In the fifth example, there are two valid subsequences of brackets: "[[][]]" and "[][][]". Both have at least one nested bracket.
// In the sixth example, the valid subsequences of brackets are "[][]" and "[][[]]". Both have at least one nested bracket.







































































































