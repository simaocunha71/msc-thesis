for _, ext := range extensions {
    if strings.HasPrefix(ext, class_name) {
        return class_name + "." + ext
    }
}

return ""
}

