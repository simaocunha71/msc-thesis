    if len(text) == 0 {
        return nil
    }
    hasher := md5.New()
    hasher.Write([]byte(text))
    return hasher.Sum(nil)
}



