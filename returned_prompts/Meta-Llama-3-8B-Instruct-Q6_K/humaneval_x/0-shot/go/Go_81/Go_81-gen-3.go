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

This program defines a function `NumericalLetterGrade` that takes a slice of floats as input and returns a slice of strings, where each string is a letter grade corresponding to the GPA. It iterates over the input slice, checks the GPA against the grading table, and appends the corresponding letter grade to the result slice. Finally, it returns the result slice. In the `main` function, it tests the `NumericalLetterGrade` function with a sample input and prints the result. The output will be `["A+", "B", "C-", "C", "A-"]`.