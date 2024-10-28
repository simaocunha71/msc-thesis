```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, r := range brackets {
        if string(r) == "(" {
            stack = append(stack, r)
        } else if string(r) == ")" {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```


The `CorrectBracketing` function takes a string `brackets` as input, which is a sequence of parentheses. The function returns `true` if every opening bracket has a corresponding closing bracket and `false` otherwise.

The function uses a stack to keep track of the opening brackets. It iterates over the input string, and for each character:

* If the character is an opening bracket `(`, it is pushed onto the stack.
* If the character is a closing bracket `)`, it checks if the stack is empty. If it is, it means there is no corresponding opening bracket, so the function returns `false`. Otherwise, it pops the opening bracket from the stack.

After iterating over the entire input string, the function checks if the stack is empty. If it is, it means all opening brackets have been matched with corresponding closing brackets, so the function returns `true`. If the stack is not empty, it means there are unmatched opening brackets, so the function returns `false`.

For example, the input `"("` would return `false` because there is no corresponding closing bracket. The input `"()"` would return `true` because the opening and closing brackets are matched. The input `"(()())"` would return `true` because all opening and closing brackets are matched. The input `")(("` would return `false` because there is no corresponding closing bracket for the first opening bracket.