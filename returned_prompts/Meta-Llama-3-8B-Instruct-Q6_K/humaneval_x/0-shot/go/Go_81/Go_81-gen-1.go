```
package main

import (
	"fmt"
	"strings"
)

func NumericalLetterGrade(grades []float64) []string {
	var letterGrades []string
	for _, gpa := range grades {
		var grade string
		if gpa >= 4.0 {
			grade = "A+"
		} else if gpa > 3.7 {
			grade = "A"
		} else if gpa > 3.3 {
			grade = "A-"
		} else if gpa > 3.0 {
			grade = "B+"
		} else if gpa > 2.7 {
			grade = "B"
		} else if gpa > 2.3 {
			grade = "B-"
		} else if gpa > 2.0 {
			grade = "C+"
		} else if gpa > 1.7 {
			grade = "C"
		} else if gpa > 1.3 {
			grade = "C-"
		} else if gpa > 1.0 {
			grade = "D+"
		} else if gpa > 0.7 {
			grade = "D"
		} else if gpa > 0.0 {
			grade = "D-"
		} else {
			grade = "E"
		}
		letterGrades = append(letterGrades, grade)
	}
	return letterGrades
}

func main() {
	grades := []float64{4.0, 3.0, 1.7, 2.0, 3.5}
	result := NumericalLetterGrade(grades)
	fmt.Println(strings.Join(result, ", "))
}
```
Output:
```
A+, B, C-, C, A-
```
This program defines a function `NumericalLetterGrade` that takes a slice of GPAs as input and returns a slice of letter grades. The function iterates over the input GPAs and uses if-else statements to determine the corresponding letter grade based on the GPA. The letter grade is then appended to the `letterGrades` slice. In the `main` function, we test the `NumericalLetterGrade` function with a slice of GPAs and print the result. The output is a comma-separated string of letter grades.