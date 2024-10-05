    if text == "" {
        return nil
    } else {
        md5hash := md5.New()
        md5hash.Write([]byte(text))
        return fmt.Sprintf("%x", md5hash.Sum(nil))
    }
}



