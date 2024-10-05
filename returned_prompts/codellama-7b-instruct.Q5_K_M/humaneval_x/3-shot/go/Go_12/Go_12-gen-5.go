    if len(strings)==0 {
        return nil
    }
    longest_string := strings[0]
    for _,s := range strings {
        if len(s) > len(longest_string){
            longest_string = s
        }
    }
    return longest_string
}



