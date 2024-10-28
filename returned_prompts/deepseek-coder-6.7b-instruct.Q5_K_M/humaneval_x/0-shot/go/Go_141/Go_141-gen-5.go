    // Count the numbers in the file name
    num_count := strings.Count(file_name, "0") + strings.Count(file_name, "1") + strings.Count(file_name, "2") + strings.Count(file_name, "3") + strings.Count(file_name, "4") + strings.Count(file_name, "5") + strings.Count(file_name, "6") + strings.Count(file_name, "7") + strings.Count(file_name, "8") + strings.Count(file_name, "9")

    if num_count > 3 {
        return "No"
    }

    // Check if the file name has exactly one dot
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Split the file name into two parts before and after the dot
    parts := strings.Split(file_name, ".")

    // Check if the part before the dot starts with a letter and is not empty
    if !(strings.HasPrefix(parts[0], "a") || strings.HasPrefix(parts[0], "b") || strings.HasPrefix(parts[0], "c") || strings.HasPrefix(parts[0], "d") || strings.HasPrefix(parts[0], "e") || strings.HasPrefix(parts[0], "f") || strings.HasPrefix(parts[0], "g") || strings.HasPrefix(parts[0], "h") || strings.HasPrefix(parts[0], "i") || strings.HasPrefix(parts[0], "j") || strings.HasPrefix(parts[0], "k") || strings.HasPrefix(parts[0], "l") || strings.HasPrefix(parts[0], "m") || strings.HasPrefix(parts[0], "n") || strings.HasPrefix(parts[0], "o") || strings.HasPrefix(parts[0], "p") || strings.HasPrefix(parts[0], "q") || strings.HasPrefix(parts[0], "r") || strings.HasPrefix(parts[0], "s") || strings.HasPrefix(parts[0], "t") || strings.Has