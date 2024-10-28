    if len(file_name)<2 || len(file_name)>3+4 {
        return "No"
    }

    if strings.Count(file_name, '.') != 1 {
        return "No"
    }

    first_part := file_name[:strings.Index(file_name, '.')]
    second_part := file_name[strings.Index(file_name, '.'):]

    if len(first_part) == 0 || first_part[0] < 'a' || first_part[0] > 'z' {
        return "No"
    }

    if len(second_part) != 3 {
        return "No"
    }

    if second_part != "txt" && second_part != "exe" && second_part != "dll" {
        return "No"
    }

    return "Yes"
}



