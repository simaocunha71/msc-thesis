    result := make([]int, 0)
    for _, c := range music_string {
        if c == 'o' {
            result = append(result, 4)
        } else if c == '|' {
            if music_string[len(music_string)-1] == 'o' {
                result = append(result, 2)
            } else {
                result = append(result, 1)
            }
        }
    }
    return result
}



