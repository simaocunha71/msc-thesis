    result := make([]int, 0)
    notes := strings.Split(music_string, " ")
    for _, note := range notes {
        switch note {
        case "o":
            result = append(result, 4)
        case "o|":
            result = append(result, 2)
        case ".|":
            result = append(result, 1)
        }
    }
    return result
}

