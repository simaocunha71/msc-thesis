    result := make([]int, 0)
    note := ""
    for _, c := range music_string {
        note += string(c)
        if c == ' ' {
            switch note {
            case "o":
                result = append(result, 4)
            case "o|":
                result = append(result, 2)
            case ".|":
                result = append(result, 1)
            }
            note = ""
        }
    }
    return result
}



