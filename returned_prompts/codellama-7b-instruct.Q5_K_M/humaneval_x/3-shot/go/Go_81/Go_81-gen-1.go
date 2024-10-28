    var result []string
    for _, grade := range grades {
        if grade >= 4.0 {
            if grade >= 4.0 && grade < 4.3 {
                result = append(result, "A")
            }else if grade >= 4.3 {
                result = append(result, "A+")
            }
        }else if grade >= 3.0 {
            if grade >= 3.0 && grade < 3.3 {
                result = append(result, "B")
            }else if grade >= 3.3 && grade < 3.7 {
                result = append(result, "B+")
            }else if grade >= 3.7 {
                result = append(result, "A")
            }
        }else if grade >= 2.0 {
            if grade >= 2.0 && grade < 2.3 {
                result = append(result, "C")
            }else if grade >= 2.3 && grade < 2.7 {
                result = append(result, "C+")
            }else if grade >= 2.7 {
                result = append(result, "B")
            }
        }else if grade >= 1.0 {
            if grade >= 1.0 && grade < 1.3 {
                result = append(result, "D")
            }else if grade >= 1.3 && grade < 1.7 {
                result = append(result, "D+")
            }else if grade >= 1.7 {
                result = append(result, "C")
            }
        }else{
            result = append(result, "E")
        }
    }
    return result
}



