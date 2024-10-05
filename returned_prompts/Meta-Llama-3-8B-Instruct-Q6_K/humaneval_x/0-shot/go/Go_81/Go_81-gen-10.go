```go
package main

import (
	"fmt"
)

func NumericalLetterGrade(grades []float64) []string {
	letterGrades := make([]string, len(grades))
	for i, grade := range grades {
		if grade >= 4.0 {
			letterGrades[i] = "A+"
		} else if grade > 3.7 {
			letterGrades[i] = "A"
		} else if grade > 3.3 {
			letterGrades[i] = "A-"
		} else if grade > 3.0 {
			letterGrades[i] = "B+"
		} else if grade > 2.7 {
			letterGrades[i] = "B"
		} else if grade > 2.3 {
			letterGrades[i] = "B-"
		} else if grade > 2.0 {
			letterGrades[i] = "C+"
		} else if grade > 1.7 {
			letterGrades[i] = "C"
		} else if grade > 1.3 {
			letterGrades[i] = "C-"
		} else if grade > 1.0 {
			letterGrades[i] = "D+"
		} else if grade > 0.7 {
			letterGrades[i] = "D"
		} else if grade > 0.0 {
			letterGrades[i] = "D-"
		} else {
			letterGrades[i] = "E"
		}
	}
	return letterGrades
}

func main() {
	grades := []float64{4.0, 3.0, 1.7, 2.0, 3.5}
	fmt.Println(NumericalLetterGrade(grades)) // Output: [A+ B C+ C A-]
}
```

This program defines a function `NumericalLetterGrade` that takes a slice of `float64` as input and returns a slice of strings representing the letter grades. It iterates over the input slice, checks the GPA against the given conditions, and assigns the corresponding letter grade to the output slice. The `main` function demonstrates the usage of this function with a sample input. The output will be `["A+", "B", "C+", "C", "A-