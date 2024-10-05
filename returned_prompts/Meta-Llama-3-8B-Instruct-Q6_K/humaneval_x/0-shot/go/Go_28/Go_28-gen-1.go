    result := ""
    for _, s := range strings {
        result += s
    }
    return result
}

B:
    result := ""
    for i := 0; i < len(strings); i++ {
        result += strings[i]
    }
    return result
}

C:
    return strings[0]
}

D:
    result := strings[0]
    for i := 1; i < len(strings); i++ {
        result += strings[i]
    }
    return result
}

E:
    return strings
}

F:
    strings := strings.Join("", strings)
    return strings
}

G:
    return strings.Join(" ", strings)
}

H:
    return strings.Join("", strings[:len(strings)-1]) + strings[len(strings)-1]
}

I:
    return strings.Join(" ", strings[:len(strings)-1]) + strings[len(strings)-1]
}

J:
    strings := strings.Join("", strings[1:])
    return strings
}

K:
    return strings.Join(" ", strings[1:])
}

L:
    result := strings[0]
    for i := 1; i < len(strings); i++ {
        result += " " + strings[i]
    }
    return result
}

M:
    result := ""
    for i := 1; len(strings) > i; i++ {
        result += strings[i-1] + " "
    }
    return result[0 : len(result)-1]
}

N:
    result := ""
    for i := 1; len(strings) > i; i++ {
        result += strings[i-1] + " "
    }
    return result
}

O:
    return strings[0] + " " + strings[1:]
}

P:
    result := strings[0]
    for i := 1; i < len(strings); i++ {
        result += " " + strings[i]
    }
    return result[1:]
}

