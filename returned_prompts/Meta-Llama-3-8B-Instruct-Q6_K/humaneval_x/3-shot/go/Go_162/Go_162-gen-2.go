    if text == "" {
        return nil
    }
    hash := md5.New()
    hash.Write([]byte(text))
    bytes := hash.Sum(nil)
    return fmt.Sprintf("%x", bytes)
}