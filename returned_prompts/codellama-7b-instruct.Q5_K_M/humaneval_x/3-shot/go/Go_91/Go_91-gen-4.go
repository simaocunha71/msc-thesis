    var boredoms int = 0
    var pattern = regexp.MustCompile(`(^|[.?!])I`)
    for _, sentence := range strings.Split(S, "."){
        if pattern.MatchString(sentence){
            boredoms += 1
        }
    }
    return boredoms
}



