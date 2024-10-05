Here is the solution in Go:

```go
package main

import (
    "math"
    "strings"
)

func ParseNestedParens(paren_string string) []int {
    res := make([]int, 0, len(strings.Split(paren_string, " ")))
    for _, group := range strings.Split(paren_string, " ") {
        level := 0
        maxLevel := 0
        for _, ch := range group {
            if ch == '(' {
                level++
                if level > maxLevel {
                    maxLevel = level
                }
            } else if ch == ')' {
                level--
            }
        }
        res = append(res, maxLevel)
    }
    return res
}

func main() {
    input := "(()()) ((())) () ((())()())"
    output := ParseNestedParens(input)
    for _, level := range output {
        println(level)
    }
}
```

In this solution, we split the input string into groups separated by spaces. For each group, we iterate over the characters and keep track of the current level of nesting. When we encounter a '(', we increment the level and update the maximum level if necessary. When we encounter a ')', we decrement the level. Finally, we append the maximum level for each group to the result slice. 

In the main function, we test the solution with the given input string and print the result. The output should be `[2, 3, 1, 3]`. 