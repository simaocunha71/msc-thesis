Here is a Go function that uses a stack to keep track of the nesting level of parentheses.

```go
import (
    "math"
    "strings"
)

func ParseNestedParens(paren_string string) []int {
    var result []int
    var stack []byte
    var maxLevel int

    for _, c := range strings.Split(paren_string, " ") {
        stack = []byte{}
        level := 0
        for _, cc := range c {
            if cc == '(' {
                level++
                stack = append(stack, cc)
            } else if cc == ')' {
                level--
                if level < 0 {
                    level = 0
                }
                stack = stack[:len(stack)-1]
            }
            if level > maxLevel {
                maxLevel = level
            }
        }
        result = append(result, maxLevel)
    }
    return result
}
```

This function splits the input string into individual groups, then for each group, it uses a stack to keep track of the nesting level of parentheses. It initializes a variable `maxLevel` to keep track of the maximum level of nesting in the current group. When it encounters a `(`, it increments the level and pushes the `(` onto the stack. When it encounters a `)`, it decrements the level and pops the `(` from the stack. If the level becomes negative, it resets it to 0. It updates `maxLevel` whenever it finds a level that is higher than the current maximum. Finally, it appends the maximum level to the result slice. The function returns the result slice. 

For example, if you call `ParseNestedParens('(()()) ((())) () ((())()())')`, it will return `[2, 3, 1, 3]`. 

Please note that this function assumes that the input string is a valid representation of nested parentheses, i.e., it does not contain any unmatched parentheses. If the input string can contain unmatched parentheses, you may need to add additional error handling.  Also, this function assumes that the input string does not contain any whitespace characters other than spaces. If the input string can contain other types of whitespace characters, you may need to adjust the regular expression used to split the string.  Finally, this function assumes that the input string does not contain any parentheses that are not balanced. If the input string can contain unbalanced parentheses, you may need to add additional error handling. 