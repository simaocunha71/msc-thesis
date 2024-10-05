    result := make([]int, 0)

    for _, r := range music_string {
        if r == 'o' {
            result = append(result, 4)
        }else if r == 'o|' {
            result = append(result, 2)
        }else if r == '.' {
            result = append(result, 1)
        }
    }
    return result
}



