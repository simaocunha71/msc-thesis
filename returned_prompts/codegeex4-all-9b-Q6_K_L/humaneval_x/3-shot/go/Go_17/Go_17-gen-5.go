    result := make([]int, 0)
    tokens := strings.Split(music_string, " ")
    for _, token := range tokens {
        switch token {
        case "o":
            result = append(result, 4)
        case "o|":
            result = append(result, 2)
        case ".|":
            result = append(result, 1)
        default:
            panic("Unknown token: " + token)
        }
    }
    return result
}



