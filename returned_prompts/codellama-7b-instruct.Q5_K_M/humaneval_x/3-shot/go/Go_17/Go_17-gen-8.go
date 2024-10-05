    result := make([]int, 0)
    for _, c := range music_string {
        if c == 'o' {
            result = append(result, 4)
        }else if c == '|' {
            if len(result) == 0 {
                result = append(result, 1)
            }else{
                result[len(result) - 1] *= 2
            }
        }
    }
    return result
}



