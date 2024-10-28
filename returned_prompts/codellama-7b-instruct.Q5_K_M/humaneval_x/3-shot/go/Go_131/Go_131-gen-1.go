    var result int = 0
    for _, c := range strconv.Itoa(n) {
        i, err := strconv.Atoi(string(c))
        if err != nil{
            panic(err)
        }
        if i%2 == 1{
            result += i
        }
    }
    return result
}



