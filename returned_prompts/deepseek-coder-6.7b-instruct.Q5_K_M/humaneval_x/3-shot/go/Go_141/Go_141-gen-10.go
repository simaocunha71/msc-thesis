    if strings.Count(file_name, ".") > 1 || strings.Count(file_name, ".") == 0{
        return "No"
    }
    parts := strings.Split(file_name, ".")
    if len(parts[0]) == 0 || !strings.Contains("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", string(parts[0][0])){
        return "No"
    }
    if strings.Contains("0123456789", parts[0][:1]) || strings.Contains("0123456789", parts[0][len(parts[0])-1:]) {
        count := 0
        for _, c := range parts[0] {
            if "0123456789" == string(c) {
                count++
            }
        }
        if count > 3 {
            return "No"
        }
    }
    if parts[1] != "txt" && parts[1] != "exe" && parts[1] != "dll" {
        return "No"
    }
    return "Yes"
}



