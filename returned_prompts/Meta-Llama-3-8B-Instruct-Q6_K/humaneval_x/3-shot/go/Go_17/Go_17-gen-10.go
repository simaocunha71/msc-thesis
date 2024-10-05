    result := make([]int, 0)
    note_map := map[rune]int{'o': 4, 'o|': 2, '.|': 1}

    for _, c := range music_string {
        if c == '|' {
            continue
        }
        result = append(result, note_map[rune(c)])
    }
    return result
}