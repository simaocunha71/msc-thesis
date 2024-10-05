    var (
        name_parts = strings.Split(file_name, ".")
        name_length = len(name_parts[0])
        extension = name_parts[1]
    )

    if name_length > 3{
        return "No"
    }

    if len(name_parts) != 2 {
        return "No"
    }

    if !(name_parts[0] > "" && (name_parts[0][0] >= 'a' && name_parts[0][0] <= 'z') || (name_parts[0][0] >= 'A' && name_parts[0][0] <= 'Z')){
        return "No"
    }

    if (extension != "txt") && (extension != "exe") && (extension != "dll"){
        return "No"
    }

    return "Yes"
}



