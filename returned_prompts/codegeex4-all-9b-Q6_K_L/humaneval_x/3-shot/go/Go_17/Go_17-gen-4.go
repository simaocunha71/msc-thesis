    result := make([]int, 0)

    current_beat := 0
    for _, c := range music_string{
        if c == 'o'{
            current_beat = 4
        }else if c == '|'{
            if music_string[len(music_string)-1] == '|{
                current_beat = 0.5
            }else{
                current_beat = 2
            }
        }else if c == '.'{
            current_beat = 1
        }
        result = append(result, int(current_beat))
    }
    return result
}

