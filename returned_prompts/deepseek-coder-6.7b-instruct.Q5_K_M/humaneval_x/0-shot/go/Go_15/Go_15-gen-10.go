    s := ""
    for i:=0; i<=n; i++{
        s += strconv.Itoa(i) + " "
    }
    return s[:len(s)-1]
}

B:
    s := ""
    for i:=0; i<=n; i++{
        s += strconv.Itoa(i) + " "
    }
    return strings.TrimSuffix(s, " ")
}

C:
    var s strings.Builder
    for i:=0; i<=n; i++{
        s.WriteString(strconv.Itoa(i) + " ")
    }
    return s.String()
}

D:
    s := make([]string, n+1)
    for i:=0; i<=n; i++{
        s[i] = strconv.Itoa(i)
    }
    return strings.Join(s, " ")
}

E:
    s := make([]string, n+1)
    for i:=0; i<=n; i++{
        s[i] = strconv.Itoa(i)
    }
    return strings.Join(s, " ")
}

F:
    return strings.Replace(strings.Repeat("0 ", n+1), " ", " ", -1)
}

G:
    return strings.Repeat("0 ", n+1)
}

H:
    return strings.TrimSpace(strings.Repeat("0 ", n+1))
}

I:
    return strings.TrimSpace(strings.Repeat("01 ", n))
}

J:
    return strings.TrimSpace(strings.Repeat("0 ", n) + "0")
}

K:
    return strings.TrimSuffix(strings.Repeat("0 ", n), "