    // If there's no extensions, return the class_name
    if len(extensions) == 0 {
        return class_name
    }

    // Create a map of the extensions, with the number of uppercase letters as the key
    // and the extension as the value.
    extension_map := make(map[int]string)
    for _, extension := range extensions {
        extension_map[getUppercaseLetters(extension)] = extension
    }

    // Get the highest number of uppercase letters for any extension
    highest_uppercase_letters := 0
    for key := range extension_map {
        if key > highest_uppercase_letters {
            highest_uppercase_letters = key
        }
    }

    // Get the lowercase letters of the highest number of uppercase letters extension
    highest_extension := extension_map[highest_uppercase_letters]

    // Return the class_name with the extension
    return fmt.Sprintf("%s.%s", class_name, highest_extension)
}

// Return the number of uppercase letters in the given string
func getUppercaseLetters(str string) int {
    var count int
    for _, r := range str {
        if unicode.IsUpper(r) {
            count++
        }
    }
    return count
}
