
```go
package main

import "fmt"

func NumericalLetterGrade(grades []float64) []string {
    var result []string
    for _, grade := range grades {
        if grade >= 4.0 {
            result = append(result, "A+")
        } else if grade > 3.7 {
            result = append(result, "A")
        } else if grade > 3.3 {
            result = append(result, "A-")
        } else if grade > 3.0 {
            result = append(result, "B+")
        } else if grade > 2.7 {
            result = append(result, "B")
        } else if grade > 2.3 {
            result = append(result, "B-")
        } else if grade > 2.0 {
            result = append(result, "C+")
        } else if grade > 1.7 {
            result = append(result, "C")
        } else if grade > 1.3 {
            result = append(result, "C-")
        } else if grade > 1.0 {
            result = append(result, "D+")
        } else if grade > 0.7 {
            result = append(result, "D")
        } else if grade > 0.0 {
            result = append(result, "D-")
        } else {
            result = append(result, "E")
        }
    }
    return result
}

func main() {
    fmt.Println(NumericalLetterGrade([]float64{4.0, 3, 1.7, 2, 3.5}))
}
```

The above Go code defines a function `NumericalLetterGrade` that receives a slice of `float64` values and returns a slice of strings. It uses a series of if-else conditions to determine the letter grade based on the provided GPAs and appends the result to a slice. Finally, it returns the slice of strings.

In the `main` function, an example is provided to demonstrate the usage of the `NumericalLetterGrade` function.