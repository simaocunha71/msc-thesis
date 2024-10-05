    apples := strings.Split(s, " ")[0]
    oranges := strings.Split(s, " ")[2]
    return n - (len(apples)*1 + len(oranges)*2)
}



