    count := strings.Count(file_name, ".")
    if count != 1 || strings.HasSuffix(file_name, ".txt") || strings.HasSuffix(file_name, ".exe") || strings.HasSuffix(file_name, ".dll") {
        if file_name[0:1] >= 'a' && file_name[0:1] <= 'z' || file_name[0:1] >= 'A' && file_name[0:1] <= 'Z' {
            count_digits := strings.Count(file_name, "0") + strings.Count(file_name, "1") + strings.Count(file_name, "2") + strings.Count(file_name, "3") + strings.Count(file_name, "4") + strings.Count(file_name, "5") + strings.Count(file_name, "6") + strings.Count(file_name, "7") + strings.Count(file_name, "8") + strings.Count(file_name, "9")
            if count_digits <= 3 {
                return "Yes"
            }
        }
    }
    return "No"
}



