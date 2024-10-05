    var result = make([]string, 0)
    for _, grade := range grades {
        switch {
        case grade == 4.0:
            result = append(result, "A+")
        case grade > 3.7:
            result = append(result, "A")
        case grade > 3.3:
            result = append(result, "A-")
        case grade > 3.0:
            result = append(result, "B+")
        case grade > 2.7:
            result = append(result, "B")
        case grade > 2.3:
            result = append(result, "B-")
        case grade > 2.0:
            result = append(result, "C+")
        case grade > 1.7:
            result = append(result, "C")
        case grade > 1.3:
            result = append(result, "C-")
        case grade > 1.0:
            result = append(result, "D+")
        case grade > 0.7:
            result = append(result, "D")
        case grade > 0.0:
            result = append(result, "D-")
        default:
            result = append(result, "E")
        }
    }
    return result
}



