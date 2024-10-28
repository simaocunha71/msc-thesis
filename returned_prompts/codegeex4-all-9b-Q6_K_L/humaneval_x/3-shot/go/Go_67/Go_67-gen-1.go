    apple, _ := strconv.Atoi(strings.Split(s, "apples")[0])
    orange, _ := strconv.Atoi(strings.Split(s, "oranges")[0])
    return n - apple - orange
}


