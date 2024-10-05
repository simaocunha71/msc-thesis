    dot_position := strings.Index(file_name, ".")

    if dot_position == -1 || dot_position == 0 || dot_position == len(file_name) - 1 {
        return "No"
    }

    if !((file_name[0] >= 'a' && file_name[0] <= 'z') || (file_name[0] >= 'A' && file_name[0] <= 'Z')) {
        return "No"
    }

    for i := 1; i < dot_position; i++ {
        if file_name[i] >= '0' && file_name[i] <= '9' {
            return "No"
        }
    }

    suffix := file_name[dot_position + 1:]

    if suffix != "txt" && suffix != "exe" && suffix != "dll" {
        return "No"
    }

    return "Yes"
}

