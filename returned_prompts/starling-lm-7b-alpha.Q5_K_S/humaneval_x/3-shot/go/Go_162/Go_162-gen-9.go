    if len(text) == 0 {
        return nil
    }

    md5Hash := md5.New()
    md5Hash.Write([]byte(text))
    return fmt.Sprintf("%x", md5Hash.Sum(nil))
}



