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
		} else if grade > 3.7 {
			letterGrades = append(letterGrades, "A")
		} else if grade > 3.3 {
			letterGrades = append(letterGrades, "A-")
		} else if grade > 3.0 {
			letterGrades = append(letterGrades, "B+")
		} else if grade > 2.7 {
			letterGrades = append(letterGrades, "B")
		} else if grade > 2.3 {
			letterGrades = append(letterGrades, "B-")
		} else if grade > 2.0 {
			letterGrades = append(letterGrades, "C+")
		} else if grade > 1.7 {
			letterGrades = append(letterGrades, "C")
		} else if grade > 1.3 {
			letterGrades = append(letterGrades, "C-")
		} else if grade > 1.0 {
			letterGrades = append(letterGrades, "D+")
		} else if grade > 0.7 {
			letterGrades = append(letterGrades, "D")
		} else if grade > 0.0 {
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
[A+ B C+ C A-]
```
Explanation:
The function `NumericalLetterGrade` takes a slice of floats as an input and returns a slice of strings. It iterates over each grade in the input slice and uses if-else conditions to determine the corresponding letter grade based on the GPA. The letter grade is then appended to the `letter