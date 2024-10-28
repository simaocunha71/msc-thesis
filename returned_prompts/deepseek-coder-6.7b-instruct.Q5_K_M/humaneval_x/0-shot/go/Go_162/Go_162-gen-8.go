    if text == "" {
        return nil
    }

    hasher := md5.New()
    hasher.Write([]byte(text))
    return fmt.Sprintf("%x", hasher.Sum(nil))
}


