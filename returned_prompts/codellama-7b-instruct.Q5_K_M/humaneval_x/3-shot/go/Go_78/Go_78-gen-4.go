    var result int = 0

    for _, c := range num {
        switch string(c) {
        case "2":
            result += 1
        case "3":
            result += 1
        case "5":
            result += 1
        case "7":
            result += 1
        case "B":
            result += 1
        case "D":
            result += 1
        }
    }
    return result
}



