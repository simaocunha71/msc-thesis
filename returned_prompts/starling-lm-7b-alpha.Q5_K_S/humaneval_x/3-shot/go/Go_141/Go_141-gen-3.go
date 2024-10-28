    var result string
    var first_part_length int
    var second_part_length int
    var third_part_length int
    var first_part_digits int
    var is_first_part_empty bool

    if strings.Index(file_name, ".") == -1 {
        return "No"
    }

    if first_part := strings.Split(file_name, "."); first_part != nil {
        if len(first_part) != 1 {
            return "No"
        }
        first_part_length = len(first_part[0])
        is_first_part_empty = first_part_length == 0
        first_part_digits = strings.Count(first_part[0], "0123456789")
        if first_part_digits > 3 {
            return "No"
        }
        if !is_first_part_empty && !is_lower_case(first_part[0][0]) && !is_upper_case(first_part[0][0]) {
            return "No"
        }
    } else {
        return "No"
    }

    if second_part := strings.Split(file_name, ".")[1]; second_part != "" {
        second_part_length = len(second_part)
        if second_part_length != 3 && second_part_length != 4 {
            return "No"
        }
    } else {
        return "No"
    }

    if third_part := strings.Split(file_name, ".")[2]; third_part != "" {
        third_part_length = len(third_part)
        if third_part_length != 3 && third_part_length != 4 {
            return "No"
        }
        if third_part != "txt" && third_part != "exe" && third_part != "dll" {
            return "No"
        }
    } else {
        return "No"
    }

    result = "Yes"
    return result
}



