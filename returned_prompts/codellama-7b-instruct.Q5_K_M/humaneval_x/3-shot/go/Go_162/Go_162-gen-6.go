    if text == ""{
        return nil
    }

    bytes := []byte(text)
    hash := md5.Sum(bytes)
    return fmt.Sprintf("%x", hash)
}



