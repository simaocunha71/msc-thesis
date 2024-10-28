    // Validate if the file's name contains exactly one dot '.'
    if !strings.Contains(file_name, ".") {
        return "No"
    }
    // Split the file's name by the dot '.' and get the substrings.
    sub1 := file_name[:strings.Index(file_name, ".")]
    sub2 := file_name[strings.Index(file_name, "."):]
    // Validate if the substring before the dot is not empty and starts with a latin alphapet letter
    if len(sub1) == 0 || sub1[0] < 'a' || sub1[0] > 'z' || sub1[0] < 'A' || sub1[0] > 'Z' {
        return "No"
    }
    // Validate if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if !strings.Contains(sub2, "txt") && !strings.Contains(sub2, "exe") && !strings.Contains(sub2, "dll") {
        return "No"
    }
    // Validate if there should not be more than three digits ('0'-'9') in the file's name
    count := 0
    for _, v := range file_name {
        if v >= '0' && v <= '9' {
            count++
        }
    }
    if count > 3 {
        return "No"
    }
    return "Yes"
}

























































































































































