    m := []struct {
        r       string
        number  int
    }{
        {"i", 1},
        {"ii", 2},
        {"iii", 3},
        {"iv", 4},
        {"v", 5},
        {"vi", 6},
        {"vii", 7},
        {"viii", 8},
        {"ix", 9},
        {"x", 10},
        {"xl", 40},
        {"l", 50},
        {"lx", 60},
        {"lxx", 70},
        {"lxxxi", 80},
        {"lxxxi", 90},
        {"c", 100},
        {"cc", 200},
        {"ccc", 300},
        {"cd", 400},
        {"d", 500},
        {"dc", 600},
        {"dcc", 700},
        {"dccc", 800},
        {"dm", 900},
        {"m", 1000},
    }

    s := ""
    for _, v := range m {
        for number / v.number > 0 {
            s += v.r
            number -= v.number
        }
    }
    return s
}



