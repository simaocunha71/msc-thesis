    var counter int = 0

    for i := 0; i < len(str); i++ {
        if str[i:len(substring)+i] == substring {
            counter++
        }
    }
    return counter
}



