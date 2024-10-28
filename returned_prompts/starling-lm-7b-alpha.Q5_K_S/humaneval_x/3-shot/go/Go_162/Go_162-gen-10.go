    if len(text) == 0 {
        return nil
    }
    h := md5.New()
    h.Write([]byte(text))
    return h.Sum(nil)
}



