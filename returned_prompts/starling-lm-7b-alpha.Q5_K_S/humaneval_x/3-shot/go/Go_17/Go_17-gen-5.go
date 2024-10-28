    result := make([]int, 0)

    for _,c := range music_string {
        if c == 'o' {
            result = append(result, 4)
        }else if c == '.' {
            result = append(result, 1)
        }else if c == '|' {
            continue
        }
    }

    return result
}



