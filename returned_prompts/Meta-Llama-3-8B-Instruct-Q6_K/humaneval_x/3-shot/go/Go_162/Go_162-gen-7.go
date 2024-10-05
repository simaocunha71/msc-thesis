    if text == "" {
        return nil
    }
    md5Hash := md5.New()
    md5Hash.Write([]byte(text))
    checksum := md5Hash.Sum(nil)
    return fmt.Sprintf("%x", checksum)
}