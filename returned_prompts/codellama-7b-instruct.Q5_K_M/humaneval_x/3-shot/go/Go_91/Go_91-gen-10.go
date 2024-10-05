    var bored_count = 0
    re := regexp.MustCompile("(I|i)(\\.)|(I|i)(\\?)|(I|i)(\\!)")
    for _, match := range re.FindAllString(S, -1) {
        if re.MatchString(match) {
            bored_count += 1
        }
    }
    return bored_count
}



