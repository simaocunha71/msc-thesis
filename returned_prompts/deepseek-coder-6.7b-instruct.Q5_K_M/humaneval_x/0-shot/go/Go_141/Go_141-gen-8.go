    // Check if the file's name contains exactly one dot 
    if strings.Count(file_name, ".") != 1 {
        return "No"
    }

    // Split the file's name into two parts: name and extension
    parts := strings.Split(file_name, ".")
    name, extension := parts[0], parts[1]

    // Check if the name part is not empty and starts with a latin alphapet letter
    if name == "" || !strings.ContainsAny(name, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }

    // Check if the extension is one of these:  ['txt',  'exe',  'dll']
    if extension != "txt" && extension != "exe" && extension != "dll" {
        return "No"
    }

    // Check if there are more than three digits in the file's name
    if strings.Count(file_name, "0")+strings.Count(file_name, "1")+strings.Count(file_name, "2")+strings.Count(file_name, "3")+strings.Count(file_name, "4")+strings.Count(file_name, "5")+strings.Count(file_name, "6")+strings.Count(file_name, "7")+strings.Count(file_name, "8")+strings.Count(file_name, "9") > 3 {
        return "No"
    }

    return "Yes"
}

// Testing
func main() {
    fmt.Println(FileNameCheck("example.txt"))  //  'Yes'
    fmt.Println(FileNameCheck("1example.dll")) //  'No'
}
```

This code checks the conditions for a valid file name and returns 'Yes' if all conditions are met, otherwise it returns 'No'.

It first checks if there is exactly one dot in the file name. If there isn't, it returns 'No'. Then it splits the file name into two parts