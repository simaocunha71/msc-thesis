Here is the solution using a stack to keep track of the nesting level:
```go
import (
    "math"
    "strings"
)

func ParseNestedParens(paren_string string) []int {
    var result []int
    var stack []int
    var maxLevel int
    var currentLevel int

    for _, c := range strings.Split(paren_string, " ") {
        for _, ch := range c {
            if ch == '(' {
                stack = append(stack, currentLevel + 1)
                if currentLevel+1 > maxLevel {
                    maxLevel = currentLevel + 1
                }
                currentLevel++
            } else if ch == ')' {
                if len(stack) > 0 {
                    currentLevel = stack[len(stack)-1] - 1
                    stack = stack[:len(stack)-1]
                }
            }
        }
        result = append(result, maxLevel)
        maxLevel = 0
        currentLevel = 0
    }
    return result
}
```
Here's an explanation of the code:

1. We initialize an empty stack and a variable `currentLevel` to keep track of the current nesting level.
2. We iterate through each character in the input string, and for each character:
	* If the character is `(`, we push the current nesting level onto the stack, increment the current nesting level, and update the maximum nesting level if necessary.
	* If the character is `)`, we pop the top element from the stack, decrement the current nesting level, and update the maximum nesting level if necessary.
3. After processing each group of parentheses, we append the maximum nesting level to the result slice and reset the maximum nesting level and current nesting level to 0.
4. Finally, we return the result slice.

You can test this function with the example input you provided:
```go
result := ParseNestedParens("(()()) ((())) () ((())()())")
fmt.Println(result) // Output: [2 3 1 3]
```
This function should correctly parse the nested parentheses and return the maximum nesting level for each group. Let me know if you have any further questions or if you'd like me to explain any part of the code in more detail!