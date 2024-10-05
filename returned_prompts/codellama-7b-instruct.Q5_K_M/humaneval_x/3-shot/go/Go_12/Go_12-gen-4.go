    if len(strings) == 0{
        return nil
    }
    longest := strings[0]
    for _, string := range strings {
        if len(string) > len(longest){
            longest = string
        }
    }
    return longest
}



