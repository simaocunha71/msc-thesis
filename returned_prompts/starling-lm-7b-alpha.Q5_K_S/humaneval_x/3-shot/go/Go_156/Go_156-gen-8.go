    const (
        M = 1000
        D = 500
        C = 100
        L = 50
        X = 10
        V = 5
        I = 1
    )

    var result []rune

    for number >= M {
        result = append(result, 'm')
        number -= M
    }
    for number >= D {
        result = append(result, 'd')
        number -= D
    }
    for number >= C {
        result = append(result, 'c')
        number -= C
    }
    for number >= L {
        result = append(result, 'l')
        number -= L
    }
    for number >= X {
        result = append(result, 'x')
        number -= X
    }
    for number >= V {
        result = append(result, 'v')
        number -= V
    }
    for number >= I {
        result = append(result, 'i')
        number -= I
    }

    return string(result)
}



