    result := 0
    for _, v := range nums {
        if v > 10 {
            str := strconv.Itoa(v)
            first := str[0]
            last := str[len(str)-1]
            if first != "0" && last != "0" && first == last && (first == "1" || first == "3" || first == "5" || first == "7" || first == "9") {
                result ++
            }
        }
    }
    return result
}



