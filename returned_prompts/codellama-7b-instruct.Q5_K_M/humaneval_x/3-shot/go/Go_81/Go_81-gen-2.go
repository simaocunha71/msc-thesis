    result := make([]string, 0)

    for _, grade := range grades {
        if grade >= 4.0 {
            result = append(result, "A+")
        }else if grade >= 3.7 {
            result = append(result, "A")
        }else if grade >= 3.3 {
            result = append(result, "A-")
        }else if grade >= 3.0 {
            result = append(result, "B+")
        }else if grade >= 2.7 {
            result = append(result, "B")
        }else if grade >= 2.3 {
            result = append(result, "B-")
        }else if grade >= 2.0 {
            result = append(result, "C+")
        }else if grade >= 1.7 {
            result = append(result, "C")
        }else if grade >= 1.3 {
            result = append(result, "C-")
        }else if grade >= 1.0 {
            result = append(result, "D+")
        }else if grade >= 0.7 {
            result = append(result, "D")
        }else if grade >= 0.0 {
            result = append(result, "D-")
        }else{
            result = append(result, "E")
        }
    }
    return result
}



