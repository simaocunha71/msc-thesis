
```go
package main

import "fmt"

func NumericalLetterGrade(grades []float64) []string {
	var result []string
	for _, gpa := range grades {
		if gpa >= 4.0 {
			result = append(result, "A+")
		} else if gpa > 3.7 {
			result = append(result, "A")
		} else if gpa > 3.3 {
			result = append(result, "A-")
		} else if gpa > 3.0 {
			result = append(result, "B+")
		} else if gpa > 2.7 {
			result = append(result, "B")
		} else if gpa > 2.3 {
			result = append(result, "B-")
		} else if gpa > 2.0 {
			result = append(result, "C+")
		} else if gpa > 1.7 {
			result = append(result, "C")
		} else if gpa > 1.3 {
			result = append(result, "C-")
		} else if gpa > 1.0 {
			result = append(result, "D+")
		} else if gpa > 0.7 {
			result = append(result, "D")
		} else if gpa > 0.0 {
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

This code defines a function `NumericalLetterGrade` that takes in an array of `float64` values (representing GPAs) and returns an array of strings (representing letter grades). 

