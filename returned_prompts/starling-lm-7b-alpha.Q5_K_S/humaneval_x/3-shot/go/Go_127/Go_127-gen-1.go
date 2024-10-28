    a := interval1[0]
    b := interval1[1]
    c := interval2[0]
    d := interval2[1]

    if a > b {
        a,b = b,a
    }

    if c > d {
        c,d = d,c
    }

    if b < c {
        return "NO"
    }

    if d < a {
        return "NO"
    }

    if b < d {
        return "YES"
    }

    return "NO"
}



