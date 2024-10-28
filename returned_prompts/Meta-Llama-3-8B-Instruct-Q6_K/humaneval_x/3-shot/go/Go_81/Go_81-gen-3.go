    result := make([]string, 0)
    for _, g := range grades {
        if g >= 4.0 {
            result = append(result, "A+")
        } else if g >= 3.7 {
            result = append(result, "A")
        } else if g >= 3.3 {
            result = append(result, "A-")
        } else if g >= 3.0 {
            result = append(result, "B+")
        } else if g >= 2.7 {
            result = append(result, "B")
        } else if g >= 2.3 {
            result = append(result, "B-")
        } else if g >= 2.0 {
            result = append(result, "C+")
        } else if g >= 1.7 {
            result = append(result, "C")
        } else if g >= 1.3 {
            result = append(result, "C-")
        } else if g >= 1.0 {
            result = append(result, "D+")
        } else if g >= 0.7 {
            result = append(result, "D")
        } else if g >= 0.0 {
            result = append(result, "D-")
        } else {
            result = append(result, "E")
        }
    }
    return result
}