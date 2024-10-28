    var apples,oranges,mangoes int
    split := strings.Split(s," ")
    for _,v := range split{
        if v[0]=='a'{
            apples += len(v[1:])
        }else if v[0]=='o'{
            oranges += len(v[1:])
        }else {
            mangoes = len(v)
        }
    }
    return n - apples - oranges - mangoes
}



