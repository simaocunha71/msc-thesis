    if len(strings)==0{
        return nil
    }
    max := 0
    longest := ""
    for _, str := range strings {
        if len(str) > max {
            max = len(str)
            longest = str
        }
    }
    return longest
}



