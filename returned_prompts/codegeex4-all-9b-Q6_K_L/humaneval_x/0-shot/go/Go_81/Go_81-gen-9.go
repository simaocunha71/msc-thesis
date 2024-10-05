```go
func NumericalLetterGrade(grades []float64) []string {
    res := make([]string, len(grades))
    for i, gpa := range grades {
        switch {
        case gpa == 4.0:
            res[i] = "A+"
        case gpa > 3.7:
            res[i] = "A"
        case gpa > 3.3:
            res[i] = "A-"
        case gpa > 3.0:
            res[i] = "B+"
        case gpa > 2.7:
            res[i] = "B"
        case gpa > 2.3:
            res[i] = "B-"
        case gpa > 2.0:
            res[i] = "C+"
        case gpa > 1.7:
            res[i] = "C"
        case gpa > 1.3:
            res[i] = "C-"
        case gpa > 1.0:
            res[i] = "D+"
        case gpa > 0.7:
            res[i] = "D"
        case gpa > 0.0:
            res[i] = "D-"
        default:
            res[i] = "E"
        }
    }
    return res
}
```
