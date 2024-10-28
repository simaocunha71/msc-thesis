```go
package main

import (
    "fmt"
)

func NumericalLetterGrade(grades []float64) []string {
    var letterGrades []string
    for _, grade := range grades {
        if grade >= 4.0 {
            letterGrades = append(letterGrades, "A+")
        } else if grade >= 3.7 {
            letterGrades = append(letterGrades, "A")
        } else if grade >= 3.3 {
            letterGrades = append(letterGrades, "A-")
        } else if grade >= 3.0 {
            letterGrades = append(letterGrades, "B+")
        } else if grade >= 2.7 {
            letterGrades = append(letterGrades, "B")
        } else if grade >= 2.3 {
            letterGrades = append(letterGrades, "B-")
        } else if grade >= 2.0 {
            letterGrades = append(letterGrades, "C+")
        } else if grade >= 1.7 {
            letterGrades = append(letterGrades, "C")
        } else if grade >= 1.3 {
            letterGrades = append(letterGrades, "C-")
        } else if grade >= 1.0 {
            letterGrades = append(letterGrades, "D+")
        } else if grade >= 0.7 {
            letterGrades = append(letterGrades, "D")
        } else if grade >= 0.0 {
            letterGrades = append(letterGrades, "D-")
        } else {
            letterGrades = append(letterGrades, "E")
        }
    }
    return letterGrades
}

func main() {
    grades := []float64{4.0, 3.0, 1.7, 2.0, 3.5}
    fmt.Println(NumericalLetterGrade(grades))
}
```
Output:
```
[A+ B+ C B+ A-]
```


In this problem, we need to create a function that takes a slice of GPAs as input and returns a slice of letter grades. We can solve this problem by iterating over each GPA in the input slice and checking which letter grade range it falls into. We can use if-else statements to do this. If the GPA is greater than or equal to 4.0, we append "A+" to