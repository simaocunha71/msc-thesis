    if text == "" {
        return nil
    }

    hash := md5.New()
    hash.Write([]byte(text))
    return fmt.Sprintf("%x", hash.Sum(nil))
}
