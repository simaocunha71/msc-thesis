package main

import (
    "fmt"
)

func MatchParens(lst []string) string {
    count := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                count++
            } else if c == ')' {
                count--
            }
        }
        if count < 0 {
            return "No"
        }
    }
    if count == 0 {
        return "Yes"
    }
    return "No"
}

func main() {
    fmt.Println(MatchParens([]string{"()(", ")"})) // Yes
    fmt.Println(MatchParens([]string{")", ")"}))     // No
}

```go
package main

import "fmt"

func MatchParens(lst []string) string {
    count := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                count++
            } else if c == ')' {
                count--
            }
        }
        if count < 0 {
            return "No"
        }
    }
    if count == 0 {
        return "Yes"
    }
    return "No"
}

func main() {
    fmt.Println(MatchParens([]string{"()(", ")"})) // Yes
    fmt.Println(MatchParens([]string{")", ")"}))     // No
}
```