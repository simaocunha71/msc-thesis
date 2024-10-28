    count_digit := 0
    for _, c := range file_name {
        if '0' <= c && c <= '9' {
            count_digit += 1
        }
    }
    if count_digit > 3 {
        return "No"
    }
    dot_index := strings.Index(file_name, ".")
    if dot_index == -1 || dot_index == 0 || dot_index == len(file_name)-1 {
        return "No"
    }
    if !(('a' <= file_name[0] && file_name[0] <= 'z') || ('A' <= file_name[0] && file_name[0] <= 'Z')) {
        return "No"
    }
    extension := file_name[dot_index+1:]
    if extension != "txt" && extension != "exe" && extension != "dll" {
        return "No"
    }
    return "Yes"
}



