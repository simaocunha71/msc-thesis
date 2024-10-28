    result := make([]int, 0)
    notes := []rune(music_string)
    beats := 0

    for _, note := range notes {
        switch note {
        case 'o':
            beats += 4
        case 'o|':
            beats += 2
        case '.|':
            beats += 1
        }
        if beats > 0 {
            result = append(result, beats)
            beats = 0
        }
    }
    return result
}