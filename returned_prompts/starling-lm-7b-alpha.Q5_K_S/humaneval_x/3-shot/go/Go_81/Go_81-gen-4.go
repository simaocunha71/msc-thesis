    result := make([]string, 0)
    for _, v := range grades {
        if v >= 4.0 {
            result = append(result, "A+")
        } else if v >= 3.7 {
            result = append(result, "A")
        } else if v >= 3.3 {
            result = append(result, "A-")
        } else if v >= 3.0 {
            result = append(result, "B+")
        } else if v >= 2.7 {
            result = append(result, "B")
        } else if v >= 2.3 {
            result = append(result, "B-")
        } else if v >= 2.0 {
            result = append(result, "C+")
        } else if v >= 1.7 {
            result = append(result, "C")
        } else if v >= 1.3 {
            result = append(result, "C-")
        } else if v >= 1.0 {
            result = append(result, "D+")
        } else if v >= 0.7 {
            result = append(result, "D")
        } else if v >= 0.0 {
            result = append(result, "D-")
        } else if v >= -0.0 {
            result = append(result, "E")
        }
    }
    return result
}















































































































































































