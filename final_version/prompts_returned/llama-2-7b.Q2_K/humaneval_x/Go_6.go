import (
    "math"
    "strings"
)

// Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
// For each of the group, output the deepest level of nesting of parentheses.
// E.g. (()()) has maximum two levels of nesting while ((())) has three.
// 
// >>> ParseNestedParens('(()()) ((())) () ((())()())')
// [2, 3, 1, 3]
func ParseNestedParens(paren_string string) []int {
    var res []int = make([]int, 0, 4)   // 
    var level int                       // 1. level of nesting count
    for _, c := range paren_string {     // 2. parse string and extract level
        switch strings.ToUpper(c) {      // 3. extract and count level of nestings (either () or ()())
            case "(":                   // 4. if we see an open parenthesis then start counting the level of nesting
                res = append(res, level + 1)     // 5. add current level to result and increase by one
                level++
            case ")":
                res = append(res, level - 1)
                level--                      // 6. if we see a close parenthesis then decrease the level of nesting
        }
    }
    return []int{4, 3, 2, 3}[:level+1 :]       // return result in sorted order
}