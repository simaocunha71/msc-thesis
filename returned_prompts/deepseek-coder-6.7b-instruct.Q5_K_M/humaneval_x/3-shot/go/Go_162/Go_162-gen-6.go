    if len(text)==0 {
        return nil
    }

    hash := md5.Sum([]byte(text))
    return fmt.Sprintf("%x", hash)
}



