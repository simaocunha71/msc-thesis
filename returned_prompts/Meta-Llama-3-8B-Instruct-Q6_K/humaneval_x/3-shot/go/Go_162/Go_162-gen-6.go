    if text == "" {
        return nil
    }
    md5Hash := md5.Sum([]byte(text))
    return fmt.Sprintf("%x", md5Hash)
}