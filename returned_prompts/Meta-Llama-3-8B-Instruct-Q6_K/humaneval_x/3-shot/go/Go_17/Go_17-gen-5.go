    result := make([]int, 0)
    note_map := map[string]int{
        "o": 4,
        "o|": 2,
        ".|": 1,
    }

    for _, note := range strings.Split(music_string, " ") {
        result = append(result, note_map[note])
    }
    return result
}