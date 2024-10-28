    if text == "" {
        return nil
    } else {
        hash := md5.Sum([]byte(text))
        return fmt.Sprintf("%x", hash)
    }
}



