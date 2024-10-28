
```go
package main

import "fmt"

func NumericalLetterGrade(grades []float64) []string {
    result := []string{}
    for _, grade := range grades {
        switch {
        case grade >= 4.0:
            result = append(result, "A+")
        case grade >= 3.7:
            result = append(result, "A")
        case grade >= 3.3:
            result = append(result, "A-")
        case grade >= 3.0:
            result = append(result, "B+")
        case grade >= 2.7:
            result = append(result, "B")
        case grade >= 2.3:
            result = append(result, "B-")
        case grade >= 2.0:
            result = append(result, "C+")
        case grade >= 1.7:
            result = append(result, "C")
        case grade >= 1.3:
            result = append(result, "C-")
        case grade >= 1.0:
            result = append(result, "D+")
        case grade >= 0.7:
            result = append(result, "D")
        case grade >= 0.0:
            result = append(result, "D-")
        case grade >= 0.0:
            result = append(result, "E")
        }
    }
    return result
}

func main() {
    fmt.Println(NumericalLetterGrade([]float64{4.0, 3, 1.7, 2, 3.5}))
    // => ["A+", "B", "C-", "C", "A-"]
}
```

In this problem, we are given a slice of float64 representing GPAs of some students. We have to write a function that will return a slice of strings representing the letter grade of each GPA. We have a table that shows the mapping of GPA to letter grade.

In the code above, we define a function called `NumericalLetterGrade` that takes a slice of float64 (representing GPAs