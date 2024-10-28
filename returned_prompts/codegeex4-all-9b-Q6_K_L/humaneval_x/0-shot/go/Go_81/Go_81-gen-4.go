```go
func NumericalLetterGrade(grades []float64) []string {
    var result []string
    for _, gpa := range grades {
        switch {
        case gpa >= 4.0:
            result = append(result, "A+")
        case gpa > 3.7:
            result = append(result, "A")
        case gpa > 3.3:
            result = append(result, "A-")
        case gpa > 3.0:
            result = append(result, "B+")
        case gpa > 2.7:
            result = append(result, "B")
        case gpa > 2.3:
            result = append(result, "B-")
        case gpa > 2.0:
            result = append(result, "C+")
        case gpa > 1.7:
            result = append(result, "C")
        case gpa > 1.3:
            result = append(result, "C-")
        case gpa > 1.0:
            result = append(result, "D+")
        case gpa > 0.7:
            result = append(result, "D")
        case gpa > 0.0:
            result = append(result, "D-")
        default:
            result = append(result, "E")
        }
    }
    return result
}
```
