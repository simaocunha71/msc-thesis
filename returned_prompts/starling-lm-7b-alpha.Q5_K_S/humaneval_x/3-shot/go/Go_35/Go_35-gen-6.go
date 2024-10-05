    result := l[0]
    for _, x := range l {
        if x > result {
            result = x
        }
    }
    return result
}



