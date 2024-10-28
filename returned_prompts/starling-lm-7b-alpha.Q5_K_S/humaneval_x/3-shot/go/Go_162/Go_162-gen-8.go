    if text == "" {
        return nil
    }
    hasher := md5.New()
    _, _ = fmt.Fprint(hasher, []byte(text))
    return hasher.Sum(nil)
}



