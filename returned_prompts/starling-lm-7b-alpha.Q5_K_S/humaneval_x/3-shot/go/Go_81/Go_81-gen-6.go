    result := make([]string, len(grades))

    for i, v := range grades {
        if v > 4.0 {
            result[i] = "A+"
        }else if v > 3.7 {
            result[i] = "A"
        }else if v > 3.3 {
            result[i] = "A-"
        }else if v > 3.0 {
            result[i] = "B+"
        }else if v > 2.7 {
            result[i] = "B"
        }else if v > 2.3 {
            result[i] = "B-"
        }else if v > 2.0 {
            result[i] = "C+"
        }else if v > 1.7 {
            result[i] = "C"
        }else if v > 1.3 {
            result[i] = "C-"
        }else if v > 1.0 {
            result[i] = "D+"
        }else if v > 0.7 {
            result[i] = "D"
        }else if v > 0.0 {
            result[i] = "D-"
        }else {
            result[i] = "E"
        }
    }

    return result
}



