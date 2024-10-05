    var mango int
    var apples int
    var oranges int

    for _, v := range s {
        if v == 'a' {
            apples++
        }else if v == 'o' {
            oranges++
        }else{
            mango++
        }
    }

    return n - apples - oranges
}



