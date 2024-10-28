```go
package main

import (
	"fmt"
)

func NumericalLetterGrade(grades []float64) []string {
	var letterGrades []string
	for _, gpa := range grades {
		switch {
		case gpa >= 4.0:
			letterGrades = append(letterGrades, "A+")
		case gpa > 3.7:
			letterGrades = append(letterGrades, "A")
		case gpa > 3.3:
			letterGrades = append(letterGrades, "A-")
		case gpa > 3.0:
			letterGrades = append(letterGrades, "B+")
		case gpa > 2.7:
			letterGrades = append(letterGrades, "B")
		case gpa > 2.3:
			letterGrades = append(letterGrades, "B-")
		case gpa > 2.0:
			letterGrades = append(letterGrades, "C+")
		case gpa > 1.7:
			letterGrades = append(letterGrades, "C")
		case gpa > 1.3:
			letterGrades = append(letterGrades, "C-")
		case gpa > 1.0:
			letterGrades = append(letterGrades, "D+")
		case gpa > 0.7:
			letterGrades = append(letterGrades, "D")
		case gpa > 0.0:
			letterGrades = append(letterGrades, "D-")
		default:
			letterGrades = append(letterGrades, "E")
		}
	}
	return letterGrades
}

func main() {
	grades := []float64{4.0, 3, 1.7, 2, 3.5}
	fmt.Println(NumericalLetterGrade(grades)) // Output: [A+ B C- C A-]
}
```


The above code defines a function called `NumericalLetterGrade` that takes a slice of floating point numbers as an argument. It iterates over each number in the slice and uses a switch statement to determine the corresponding letter grade based on the GPA. The letter grade is then appended to a slice of strings. Finally, the function returns the slice of letter grades.

In the `main` function, we test the `NumericalLetter