    if len(text) == 0 {
        return nil
    }
    hasher := md5.New()
    _, _ = hasher.Write([]byte(text))
    return hasher.Sum(nil)
}



