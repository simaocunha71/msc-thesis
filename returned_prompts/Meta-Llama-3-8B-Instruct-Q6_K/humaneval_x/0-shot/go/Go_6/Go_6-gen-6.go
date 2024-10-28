Here is the solution using Go language:

```go
package main

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
    res := make([]int, 0)
    for _, group := range strings.Split(paren_string, " ") {
        depth := 0
        maxDepth := 0
        for _, c := range group {
            if string(c) == "(" {
                depth++
                maxDepth = math.Max(maxDepth, depth)
            } else if string(c) == ")" {
                depth--
            }
        }
        res = append(res, maxDepth)
    }
    return res
}

func main() {
    result := ParseNestedParens("(()()) ((())) () ((())()())")
    for _, v := range result {
        println(v)
    }
}
```

This program defines a function `ParseNestedParens` that takes a string of parentheses as input and returns a slice of integers. The slice contains the deepest level of nesting of parentheses for each group of parentheses in the input string. 

In the `main` function, we call `ParseNestedParens` with the input string and print the result.

The `ParseNestedParens` function splits the input string into groups of parentheses using the `strings.Split` function. Then for each group, it iterates over the characters in the group and keeps track of the current depth of nesting using a variable `depth`. It also keeps track of the maximum depth of nesting seen so far in the group using a variable `maxDepth`. When it encounters a closing parenthesis, it decreases the `depth` by 1. At the end of the group, it appends the `maxDepth` to the result slice. 

The time complexity of this program is O(n), where n is the total number of characters in the input string. The space complexity is O(n), where n is the number of groups of parentheses in the input string. 