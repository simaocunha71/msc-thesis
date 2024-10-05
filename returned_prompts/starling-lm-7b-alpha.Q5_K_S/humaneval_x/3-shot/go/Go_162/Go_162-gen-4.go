    if len(text) == 0 {
        return nil
    }
    hasher := md5.New()
    _, err := hasher.Write([]byte(text))
    if err != nil {
        fmt.Println(err)
    }
    return fmt.Sprintf("%x", hasher.Sum(nil))
}



