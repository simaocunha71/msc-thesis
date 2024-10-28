
func NumericalLetterGrade(grades []float64) []string {
    res := make([]string, len(grades))
    for i, g := range grades {
        switch {
        case g > 4.0:
            res[i] = "A+"
        case g > 3.7:
            res[i] = "A"
        case g > 3.3:
            res[i] = "A-"
        case g > 3.0:
            res[i] = "B+"
        case g > 2.7:
            res[i] = "B"
        case g > 2.3:
            res[i] = "B-"
        case g > 2.0:
            res[i] = "C+"
        case g > 1.7:
            res[i] = "C"
        case g > 1.3:
            res[i] = "C-"
        case g > 1.0:
            res[i] = "D+"
        case g > 0.7:
            res[i] = "D"
        case g > 0.0:
            res[i] = "D-"
        default:
            res[i] = "E"
        }
    }
    return res
}




































































































































































































