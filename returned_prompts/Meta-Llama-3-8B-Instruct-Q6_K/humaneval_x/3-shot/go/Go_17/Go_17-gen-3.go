    result := make([]int, 0)
    notes := strings.Split(music_string, " ")
    for _, note := range notes {
        if strings.HasSuffix(note, "|") {
            if strings.HasSuffix(note, "o|") {
                result = append(result, 2)
            } else {
                result = append(result, 1)
            }
        } else {
            result = append(result, 4)
        }
    }
    return result
}