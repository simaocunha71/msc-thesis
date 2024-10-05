    result := make([]int, 0)
    for _, r := range music_string {
        switch r {
        case 'o':
            result = append(result, 4)
        case 'o|':
            result = append(result, 2)
        case '.':
            result = append(result, 1)
        }
    }
    return result
}



