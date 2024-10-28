    var result int

    for _, c := range num {
        switch c {
        case '2', '3', '5', '7', 'B', 'D':
            result += 1
        }
    }
    return result
}



