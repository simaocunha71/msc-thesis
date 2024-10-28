    xn := strings.Split(x, "/")
    xnum, _ := strconv.Atoi(xn[0])
    xden, _ := strconv.Atoi(xn[1])

    nn := strings.Split(n, "/")
    nnum, _ := strconv.Atoi(nn[0])
    nden, _ := strconv.Atoi(nn[1])

    return (xnum * nden) == (nnum * xden)
}



