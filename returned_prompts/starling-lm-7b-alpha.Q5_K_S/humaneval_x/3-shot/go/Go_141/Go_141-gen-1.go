    count_digits := 0
    for _, c := range file_name {
        if c >= '0' && c <= '9' {
            count_digits += 1
        }
        if count_digits > 3 {
            return "No"
        }
    }

    dot_index := strings.IndexByte(file_name, '.')
    if dot_index == -1 {
        return "No"
    }
    if len(file_name) - dot_index < 4 {
        return "No"
    }

    before_dot := file_name[:dot_index]
    if len(before_dot) == 0 {
        return "No"
    }
    if before_dot[0] < 'a' || before_dot[0] > 'z' {
        return "No"
    }
    if before_dot[0] < 'A' || before_dot[0] > 'Z' {
        return "No"
    }

    after_dot := file_name[dot_index+1:]
    if after_dot != "txt" && after_dot != "exe" && after_dot != "dll" {
        return "No"
    }

    return "Yes"
}



