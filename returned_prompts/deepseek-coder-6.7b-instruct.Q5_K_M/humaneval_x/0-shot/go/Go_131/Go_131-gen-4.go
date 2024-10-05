    product := 1
    str := strconv.Itoa(n)
    for _, c := range str {
        digit, _ := strconv.Atoi(string(c))
        if digit%2 != 0 {
            product *= digit
        }
    }

    if product == 1 {
        return 0
    }

    return product
}

func main()  {
    fmt.Println(Digits(1))  // 1
    fmt.Println(Digits(4))  // 0
    fmt.Println(Digits(235))  // 15
}
*/

/*
