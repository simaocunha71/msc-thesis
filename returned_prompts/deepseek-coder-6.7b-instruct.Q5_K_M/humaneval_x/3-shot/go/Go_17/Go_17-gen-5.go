    result := make([]int, 0)

    for _, c := range music_string {
        switch c {
        case 'o':
            result = append(result, 4)
        case '|':
            result[len(result)-1] /= 2
        case '.':
            result[len(result)-1] /= 4
        }
    }

    return result
}



