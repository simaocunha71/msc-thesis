```
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, c := range brackets {
        if c == '<' {
            stack = append(stack, c)
        } else if c == '>' {
            if len(stack) == 0 || stack[len(stack)-1] != '<' {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

Explanation:
This function uses a stack to keep track of the opening brackets. It iterates over the input string, and for each character:
- If the character is '<', it pushes it onto the stack.
- If the character is '>', it checks if the stack is empty or the top of the stack is not '<'. If either condition is true, it returns false. Otherwise, it pops the top of the stack.
Finally, it returns true if the stack is empty, meaning all opening brackets have been matched with corresponding closing brackets, and false otherwise.

The time complexity is O(n), where n is the length of the input string, as it iterates over the string once. The space complexity is also O(n), as in the worst case, all characters in the string could be '<' characters.