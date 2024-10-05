    type frac struct {
        num  int
        denom int
    }

    xf, _ := strconv.Atoi(strings.Split(x, "/")[0])
    nf, _ := strconv.Atoi(strings.Split(n, "/")[0])
    xd, _ := strconv.Atoi(strings.Split(x, "/")[1])
    nd, _ := strconv.Atoi(strings.Split(n, "/")[1])

    g := gcd(xd, nd)
    xd /= g
    nd /= g

    g = gcd(xf, nf)
    g = gcd(g, xd)
    g = gcd(g, nd)
    xf /= g
    nf /= g
    nd /= g
    xd /= g

    if xf*nd == nf*xd {
        return true
    } else {
        return false
    }
    // return ((nf * xd) % nd == 0) && ((nf * xd) / nd == xf)
}

func gcd(a, b int) int {
    if a < b {
        a, b = b, a
    }
    for b != 0 {
        a, b = b, a%b
    }
    return a
}
























































































































































































