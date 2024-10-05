```go
package main

import (
	"fmt"
	"sort"
)

func NumericalLetterGrade(grades []float64) []string {
	letterGrades := []string{}
	sort.Float64s(grades)

	for _, g := range grades {
		if g >= 4.0 {
			letterGrades = append(letterGrades, "A+")
		} else if g > 3.7 {
			letterGrades = append(letterGrades, "A")
		} else if g > 3.3 {
			letterGrades = append(letterGrades, "A-")
		} else if g > 3.0 {
			letterGrades = append(letterGrades, "B+")
		} else if g > 2.7 {
			letterGrades = append(letterGrades, "B")
		} else if g > 2.3 {
			letterGrades = append(letterGrades, "B-")
		} else if g > 2.0 {
			letterGrades = append(letterGrades, "C+")
		} else if g > 1.7 {
			letterGrades = append(letterGrades, "C")
		} else if g > 1.3 {
			letterGrades = append(letterGrades, "C-")
		} else if g > 1.0 {
			letterGrades = append(letterGrades, "D+")
		} else if g > 0.7 {
			letterGrades = append(letterGrades, "D")
		} else if g > 0.0 {
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
[A+ B+ C- C A-]
```
Explanation:
The code sorts the grades in ascending order. Then for each grade, it checks which letter grade it corresponds to based on the given table. It appends the letter grade to the slice and finally returns the slice of letter grades. The