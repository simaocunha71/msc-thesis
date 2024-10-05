    if len(txt) == 0 {
        return false
    }

    if txt[len(txt)-1] >= 'a' && txt[len(txt)-1] <= 'z' || txt[len(txt)-1] >= 'A' && txt[len(txt)-1] <= 'Z' {
        return true
    }

    last_space_index := -1
    for i, v := range txt {
        if v == ' ' {
            last_space_index = i
        }
    }

    if last_space_index == len(txt)-1 {
        return true
    }else if last_space_index >= 0 {
        return txt[last_space_index+1] >= 'a' && txt[last_space_index+1] <= 'z' || txt[last_space_index+1] >= 'A' && txt[last_space_index+1] <= 'Z'
    }
    return false
}



