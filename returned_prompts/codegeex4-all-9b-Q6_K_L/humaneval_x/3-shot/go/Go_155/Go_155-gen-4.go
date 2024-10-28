    var count [2]int

    str := strconv.Itoa(num)
    for _, c := range str {
        if c == '0' || c == '2' || c == '4' || c == '6' || c == '8' {
            count[0]++
        } else if c == '1' || c == '3' || c == '5' || c == '7' || c == '9' {
            count[1]++
        }
    }
    return count
}



