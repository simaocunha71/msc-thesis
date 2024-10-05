    if text == "" {
        return nil
    }

    hasher := md5.New()
    _, err := hasher.Write([]byte(text))
    if err != nil {
        panic(err)
    }

    return fmt.Sprintf("%x", hasher.Sum(nil))
}



