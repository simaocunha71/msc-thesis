    words := strings.Split(s," ")
    apples, _ := strconv.Atoi(strings.Split(words[1]," ")[0])
    oranges, _ := strconv.Atoi(strings.Split(words[3]," ")[0])
    return n - apples - oranges
}  //Note: This code assumes that the input string is always in the format "X apples and Y oranges" where X and Y are positive integers. If this is not the case, the code may not work correctly.