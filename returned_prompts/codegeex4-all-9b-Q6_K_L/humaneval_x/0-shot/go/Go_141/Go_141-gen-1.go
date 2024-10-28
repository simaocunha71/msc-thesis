Here is a possible solution in Go:

```go
func FileNameCheck(file_name string) string {
    // Check the number of digits in the file name
    if strings.Count(file_name, "0") + strings.Count(file_name, "1") + 
       strings.Count(file_name, "2") + strings.Count(file_name, "3") + 
       strings.Count(file_name, "4") + strings.Count(file_name, "5") + 
       strings.Count(file_name, "6") + strings.Count(file_name, "7") + 
       strings.Count(file_name, "8") + strings.Count(file_name, "9") > 3 {
        return "No"
    }

    // Check the file name contains exactly one dot
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Split the file name into two parts: the name before the dot and the name after the dot
    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    name_before_dot, name_after_dot := parts[0], parts[1]

    // Check the name before the dot starts with a latin alphabet letter and is not empty
    if len(name_before_dot) == 0 || (!strings.ContainsRune(name_before_dot, 'a') && 
       !strings.ContainsRune(name_before_dot, 'b') && !strings.ContainsRune(name_before_dot, 'c') && 
       !strings.ContainsRune(name_before_dot, 'd') && !strings.ContainsRune(name_before_dot, 'e') && 
       !strings.ContainsRune(name_before_dot, 'f') && !strings.ContainsRune(name_before_dot, 'g') && 
       !strings.ContainsRune(name_before_dot, 'h') && !strings.ContainsRune(name_before_dot, 'i') && 
       !strings.ContainsRune(name_before_dot, 'j') && !strings.ContainsRune(name_before_dot, 'k') && 
       !strings.ContainsRune(name_before_dot, 'l') && !strings.ContainsRune(name_before_dot, 'm') && 
       !strings.ContainsRune(name_before_dot, 'n') && !strings.ContainsRune(name_before_dot, 'o') && 
       !strings.ContainsRune(name_before_dot, 'p') && !strings.ContainsRune(name_before_dot, 'q') && 
       !strings.ContainsRune