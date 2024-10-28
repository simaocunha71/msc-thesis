    var result int

    for _, c := range num{
        switch c {
        case 'A':
            result += 10
        case 'B':
            result += 11
        case 'C':
            result += 12
        case 'D':
            result += 13
        case 'E':
            result += 14
        case 'F':
            result += 15
        default:
            result += int(c - '0')
        }
    }

    var prime_count int

    for i := 2; i < result; i++ {
        for j := 2; j < i; j++ {
            if i % j == 0 {
                prime_count += 1
                break
            }
        }
    }
    return prime_count
}



