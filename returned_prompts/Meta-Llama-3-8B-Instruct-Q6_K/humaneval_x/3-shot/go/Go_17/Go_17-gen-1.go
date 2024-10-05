    result := make([]int, 0)
    i := 0
    for i < len(music_string) {
        if music_string[i] == 'o' {
            result = append(result, 4)
            i += 1
        } else if music_string[i] == '|' {
            i += 1
            if music_string[i] == '.' {
                result = append(result, 1)
                i += 1
            } else {
                result = append(result, 2)
                i += 1
            }
        }
    }
    return result
}