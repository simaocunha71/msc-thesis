    regexp_pattern := "(^I.*[.?!])"
    regexp_object := regexp.MustCompile(regexp_pattern)
    return len(regexp_object.FindAllString(S, -1))
}



