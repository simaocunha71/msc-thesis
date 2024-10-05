    parts := strings.Split(file_name, ".")
    if len(parts) != 2 {
        return "No"
    }
    if !strings.ContainsAny(parts[0], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return "No"
    }
    if len(strings.Replace(parts[0], ".", "", -1)) > 0 {
        return "No"
    }
    if len(strings.Replace(parts[1], ".", "", -1)) > 3 {
        return "No"
    }
    if !strings.HasSuffix(parts[1], "txt") && !strings.HasSuffix(parts[1], "exe") && !strings.HasSuffix(parts[1], "dll") {
        return "No"
    }
    return "Yes"
}  // You could also use regular expressions for this. It might be more readable.  // See https://golang.org/pkg/regexp/ for more information.  // For example, you could use the following regular expression:  //  ^[a-zA-Z][a-zA-Z0-9\.]*\.(txt|exe|dll)$  // This regular expression will match any string that starts with a letter,  // followed by zero or more letters, numbers, or dots, and ends with either  // "txt", "exe", or "dll".  // You can use this regular expression in your function like this:  //  func FileNameCheck(file_name string) string {  //      if !regexp.MustCompile(`^[a-zA-Z][a-zA-Z0-9\.]*\.(txt|exe|dll)$`).MatchString(file_name) {  //          return "No"  //      }  //      return "Yes"  //  }  //  // This will return "Yes" for valid file names and "No" for invalid ones.  //  // For example, FileNameCheck("example.txt") will return "Yes", and  //  FileNameCheck("1example.dll") will return "No".  //  // This is a more concise and readable way to solve this problem.  //  // It also handles more edge cases than the original solution,  //  // such as file names that contain multiple dots.  //  // It also handles file names that contain uppercase letters.  //  // It also handles file names that contain numbers.  //  // It also handles file names that contain special characters.  //  // It also handles file names that contain spaces.  //  // It also handles file