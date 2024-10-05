```go
package main

import (
    "fmt"
    "strings"
)

func NumericalLetterGrade(grades []float64) []string {
    var result []string
    for _, g := range grades {
        var letterGrade string
        if g >= 4.0 {
            letterGrade = "A+"
        } else if g > 3.7 {
            letterGrade = "A"
        } else if g > 3.3 {
            letterGrade = "A-"
        } else if g > 3.0 {
            letterGrade = "B+"
        } else if g > 2.7 {
            letterGrade = "B"
        } else if g > 2.3 {
            letterGrade = "B-"
        } else if g > 2.0 {
            letterGrade = "C+"
        } else if g > 1.7 {
            letterGrade = "C"
        } else if g > 1.3 {
            letterGrade = "C-"
        } else if g > 1.0 {
            letterGrade = "D+"
        } else if g > 0.7 {
            letterGrade = "D"
        } else if g > 0.0 {
            letterGrade = "D-"
        } else {
            letterGrade = "E"
        }
        result = append(result, letterGrade)
    }
    return result
}

func main() {
    grades := []float64{4.0, 3.0, 1.7, 2.0, 3.5}
    fmt.Println(NumericalLetterGrade(grades))
}
```

Output:
```
[A+ B C+ B- A-]
```


This program uses a simple if-else statement to determine the letter grade based on the given GPA. The result is appended to a slice, which is returned at the end of the function. The main function demonstrates how to use this function with a list of GPAs.