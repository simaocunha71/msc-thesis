    result := make([]string, 0, len(grades))

    for _, g := range grades {
        switch {
        case g == 4.0:
            result = append(result, "A+")
        case g > 3.7:
            result = append(result, "A")
        case g > 3.3:
            result = append(result, "A-")
        case g > 3.0:
            result = append(result, "B+")
        case g > 2.7:
            result = append(result, "B")
        case g > 2.3:
            result = append(result, "B-")
        case g > 2.0:
            result = append(result, "C+")
        case g > 1.7:
            result = append(result, "C")
        case g > 1.3:
            result = append(result, "C-")
        case g > 1.0:
            result = append(result, "D+")
        case g > 0.7:
            result = append(result, "D")
        case g > 0.0:
            result = append(result, "D-")
        default:
            result = append(result, "E")
        }
    }

    return result
}



