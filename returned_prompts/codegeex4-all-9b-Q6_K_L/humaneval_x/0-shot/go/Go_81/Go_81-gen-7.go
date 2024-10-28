```go
func NumericalLetterGrade(grades []float64) []string {
	letterGrades := make([]string, len(grades))
	for i, gpa := range grades {
		switch {
		case gpa >= 4.0:
			letterGrades[i] = "A+"
		case gpa > 3.7:
			letterGrades[i] = "A"
		case gpa > 3.3:
			letterGrades[i] = "A-"
		case gpa > 3.0:
			letterGrades[i] = "B+"
		case gpa > 2.7:
			letterGrades[i] = "B"
		case gpa > 2.3:
			letterGrades[i] = "B-"
		case gpa > 2.0:
			letterGrades[i] = "C+"
		case gpa > 1.7:
			letterGrades[i] = "C"
		case gpa > 1.3:
			letterGrades[i] = "C-"
		case gpa > 1.0:
			letterGrades[i] = "D+"
		case gpa > 0.7:
			letterGrades[i] = "D"
		case gpa > 0.0:
			letterGrades[i] = "D-"
		default:
			letterGrades[i] = "E"
		}
	}
	return letterGrades
}
```
