    result := make([]int, 0)
    current_note := 0

    for _, c := range music_string {
        if c == 'o' {
            current_note += 4
        } else if c == 'o|' {
            current_note += 2
        } else if c == '.' {
            current_note += 1
        }
        if c == '|' {
            result = append(result, current_note)
            current_note = 0
        }
    }
    result = append(result, current_note)
    return result
}