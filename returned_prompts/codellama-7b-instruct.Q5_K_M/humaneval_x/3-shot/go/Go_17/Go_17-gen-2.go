    result := make([]int, 0)

    for _, c := range music_string {
        switch c {
        case 'o':
            result = append(result, 4)
            break
        case '|':
            result = append(result, 2)
            break
        case '.':
            result = append(result, 1)
            break
        }
    }
    return result
}



