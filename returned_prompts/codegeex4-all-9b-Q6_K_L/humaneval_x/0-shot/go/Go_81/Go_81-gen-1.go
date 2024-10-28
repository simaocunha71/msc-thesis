```go
func NumericalLetterGrade(grades []float64) []string {
    var letterGrades []string
    for _, g := range grades {
        if g == 4.0 {
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
```
