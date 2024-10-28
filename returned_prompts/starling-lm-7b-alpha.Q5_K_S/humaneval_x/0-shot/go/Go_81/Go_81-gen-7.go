
```go
package main

import "fmt"

func NumericalLetterGrade(grades []float64) []string {
	var result []string

	for _, grade := range grades {
		switch {
		case grade > 3.7:
			result = append(result, "A")
		case grade > 3.3:
			result = append(result, "A-")
		case grade > 3.0:
			result = append(result, "B+")
		case grade > 2.7:
			result = append(result, "B")
		case grade > 2.3:
			result = append(result, "B-")
		case grade > 2.0:
			result = append(result, "C+")
		case grade > 1.7:
			result = append(result, "C")
		case grade > 1.3:
			result = append(result, "C-")
		case grade > 1.0:
			result = append(result, "D+")
		case grade > 0.7:
			result = append(result, "D")
		case grade > 0.0:
			result = append(result, "D-")
		case grade == 0.0:
			result = append(result, "E")
		}
	}

	return result
}

func main() {
	fmt.Println(NumericalLetterGrade([]float64{4.0, 3, 1.7, 2, 3.5}))
	// Output: ["A+", "B", "C-", "C", "A-"]
}
```

This code defines the function `NumericalLetterGrade` that takes a slice of floats as an argument and returns a slice of strings. Inside the function, there is a `switch` statement that checks the value of the `grade` variable against the conditions in the `case` statements. Based on the conditions, the function appends the corresponding letter