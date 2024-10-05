    var bin string
    sum := 0
    for N > 0 {
        remainder := N % 2
        sum += remainder
        bin = strconv.Itoa(remainder) + bin
        N /= 2
    }
    return bin
}

B:
    var bin string
    sum := 0
    for N > 0 {
        remainder := N % 2
        sum += remainder
        bin = strconv.Itoa(remainder) + bin
        N /= 2
    }
    return strconv.Itoa(sum)
}

C:
    var bin string
    sum := 0
    for N > 0 {
        remainder := N % 2
        sum += remainder
        bin = strconv.Itoa(remainder) + bin
        N /= 2
    }
    return bin
}

D:
    var bin string
    sum := 0
    for N > 0 {
        remainder := N % 2
        sum += remainder
        bin = strconv.Itoa(remainder) + bin
        N /= 2
    }
    return strconv.FormatInt(int64(sum), 2)
}

E:
    var bin string
    sum := 0
    for N > 0 {
        remainder := N % 2
        sum += remainder
        bin = strconv.Itoa(remainder) + bin
        N /= 2
    }
    return sumStr(sum)
}

F:
    var bin string
    sum := 0
    for N > 0 {
        remainder := N % 2
        sum += remainder
        bin = strconv.Itoa(remainder) + bin
        N /= 2
    }
    return fmt.Sprintf("%b", sum)
}

G:
    var bin string
    sum := 0
    for N > 0 {
        remainder := N % 2
        sum += remainder
        bin = strconv.Itoa(remainder) + bin
        N /= 2
    }
    return fmt.Sprintf("%d", sum)
}

H:
    var bin string
    sum := 0
    for N > 0 {
        remainder := N % 2
        sum += remainder
        bin = strconv.Itoa(remainder) + bin
        N /= 2
    }
    return strconv.FormatInt(int64(sum), 10)
}

I:
    var bin string
    sum := 0
    for N > 0 {
        remainder := N % 2
