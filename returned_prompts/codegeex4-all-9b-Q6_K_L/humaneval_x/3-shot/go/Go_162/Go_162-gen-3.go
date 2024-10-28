    if text == "" {
        return nil
    }
    return fmt.Sprintf("%x", md5.Sum([]byte(text)))
}

