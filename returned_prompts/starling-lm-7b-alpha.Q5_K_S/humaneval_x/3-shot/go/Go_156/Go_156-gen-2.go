    const m = 1000
    const m_s = "m"
    const c = 100
    const c_s = "c"
    const d = 50
    const d_s = "d"
    const l = 5
    const l_s = "l"
    const x = 10
    const x_s = "x"
    const i = 1
    const i_s = "i"

    var result []rune

    for number >= m {
        result = append(result, m_s...)
        number -= m
    }
    for number >= c {
        result = append(result, c_s...)
        number -= c
    }
    for number >= d {
        result = append(result, d_s...)
        number -= d
    }
    for number >= l {
        result = append(result, l_s...)
        number -= l
    }
    for number >= x {
        result = append(result, x_s...)
        number -= x
    }
    for number >= i {
        result = append(result, i_s...)
        number -= i
    }
    return string(result)
}



