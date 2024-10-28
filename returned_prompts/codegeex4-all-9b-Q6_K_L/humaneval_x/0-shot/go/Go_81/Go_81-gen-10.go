```go
func NumericalLetterGrade(grades []float64) []string {
	letterGrades := make([]string, 0, len(grades))
	for _, grade := range grades {
		switch {
		case grade == 4.0:
			letterGrades = append(letterGrades, "A+")
		case grade > 3.7:
			letterGrades = append(letterGrades, "A")
		case grade > 3.3:
			letterGrades = append(letterGrades, "A-")
		case grade > 3.0:
			letterGrades = append(letterGrades, "B+")
		case grade > 2.7:
			letterGrades = append(letterGrades, "B")
		case grade > 2.3:
			letterGrades = append(letterGrades, "B-")
		case grade > 2.0:
			letterGrades = append(letterGrades, "C+")
		case grade > 1.7:
			letterGrades = append(letterGrades, "C")
		case grade > 1.3:
			letterGrades = append(letterGrades, "C-")
		case grade > 1.0:
			letterGrades = append(letterGrades, "D+")
		case grade > 0.7:
			letterGrades = append(letterGrades, "D")
		case grade > 0.0:
			letterGrades = append(letterGrades, "D-")
		default:
			letterGrades = append(letterGrades, "E")
		}
	}
	return letterGrades
}
```
