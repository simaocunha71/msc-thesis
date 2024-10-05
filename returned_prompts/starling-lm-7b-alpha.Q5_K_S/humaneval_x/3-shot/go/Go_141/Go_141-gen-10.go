    if len(strings.Split(file_name,".")) != 2 {
        return "No"
    }
    first_part := strings.Split(file_name,".")[0]
    if len(first_part) == 0 {
        return "No"
    }
    if !strings.HasUpper(string(first_part[0])) {
        return "No"
    }
    for _, c := range first_part {
        if c < 'A' || c > 'Z' {
            return "No"
        }
    }

    second_part := strings.Split(file_name,".")[1]
    if second_part != "txt" && second_part != "exe" && second_part != "dll" {
        return "No"
    }
    return "Yes"
}



