    var numberals = strings.Split(numbers, " ")
    var numeric []int
    for _, v := range numberals {
        switch v {
        case "zero":
            numeric = append(numeric, 0)
        case "one":
            numeric = append(numeric, 1)
        case "two":
            numeric = append(numeric, 2)
        case "three":
            numeric = append(numeric, 3)
        case "four":
            numeric = append(numeric, 4)
        case "five":
            numeric = append(numeric, 5)
        case "six":
            numeric = append(numeric, 6)
        case "seven":
            numeric = append(numeric, 7)
        case "eight":
            numeric = append(numeric, 8)
        case "nine":
            numeric = append(numeric, 9)
        }
    }
    sort.Ints(numeric)
    var numberals2 = make([]string, len(numeric))
    for i, v := range numeric {
        switch v {
        case 0:
            numberals2[i] = "zero"
        case 1:
            numberals2[i] = "one"
        case 2:
            numberals2[i] = "two"
        case 3:
            numberals2[i] = "three"
        case 4:
            numberals2[i] = "four"
        case 5:
            numberals2[i] = "five"
        case 6:
            numberals2[i] = "six"
        case 7:
            numberals2[i] = "seven"
        case 8:
            numberals2[i] = "eight"
        case 9:
            numberals2[i] = "nine"
        }
    }
    result := strings.Join(numberals2, " ")
    return result
}