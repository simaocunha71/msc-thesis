    var apples, oranges int
    var fruits int
    var index int
    for index, v := range s {
        if v == 'a' {
            apples = len(s)-index
        }else if v == 'o' {
            oranges = len(s)-index
        }else if v == ' ' {
            continue
        }else {
            break
        }
    }
    fruits = n - apples - oranges
    return fruits
}



