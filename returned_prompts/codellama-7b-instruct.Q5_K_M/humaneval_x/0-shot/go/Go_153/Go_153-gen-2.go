    for _, extension := range extensions {
        if strings.HasPrefix(extension, class_name) {
            return class_name + "." + extension
        }
    }
    return ""
}

