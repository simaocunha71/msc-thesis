    result := make([]int, 0)
    i := 0
    for i < len(music_string){
        switch music_string[i:i+2] {
        case "o|":
            result = append(result, 2)
            i += 2
        case ".|":
            result = append(result, 1)
            i += 2
        case "o":
            result = append(result, 4)
            i += 1
        default:
            panic("Invalid music notation")
        }
    }
    return result
}