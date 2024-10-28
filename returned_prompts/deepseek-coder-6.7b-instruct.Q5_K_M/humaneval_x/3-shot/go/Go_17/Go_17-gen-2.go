    result := make([]int, 0)
    for _, c := range music_string {
        switch c {
        case 'o':
            result = append(result, 4)
        case '|':
            result = append(result, 2)
        case '.':
            result = append(result, 1)
        default:
            continue
        }
    }
    return result
}



