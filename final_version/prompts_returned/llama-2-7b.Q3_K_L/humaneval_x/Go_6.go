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
    // Return empty array if input is not valid.
    if (strings.Count(paren_string, "(")) != strings.Count(paren_string, ")" ) || len(paren_string) < 2 {
        return []int{}
    }
    
    // Split the string on spaces and iterate through each of the items to determine maximum level for nested parens.
    var max_level int = -1;
    var temp_arr []int
    for _, group := range strings.Fields(paren_string) {
        if (group == "("){
            max_level++
        } else if (group == ")"){
            max_level--
        }
        temp_arr = append(temp_arr, max_level) 
    }
    
    return temp_arr
}