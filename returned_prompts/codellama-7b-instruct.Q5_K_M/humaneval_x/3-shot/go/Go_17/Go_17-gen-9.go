    result := make([]int, 0)
    current_note := make([]rune, 0)
    current_length := 1

    for _, c := range music_string {
        if c == ' ' {
            result = append(result, current_length)
            current_note = make([]rune, 0)
            current_length = 1
        }else if c == 'o' {
            current_note = append(current_note, c)
            current_length = 4
        }else if c=='|' {
            current_note = append(current_note, c)
            current_length = 2
        }else if c=='.'{
            current_note = append(current_note, c)
            current_length = 1
        }else{
            // ignore anything else
        }
    }
    result = append(result, current_length)
    return result
}



