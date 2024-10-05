    s = strings.Replace(s," ","", -1)
    s = strings.Replace(s,"apples","", -1)
    s = strings.Replace(s,"oranges","", -1)
    s = strings.Replace(s,"and","", -1)
    s = strings.Replace(s,",","", -1)
    s = strings.Replace(s,".","", -1)
    s = strings.Replace(s,"-","", -1)
    s = strings.Replace(s,"_","", -1)
    s = strings.Replace(s,"!","", -1)
    s = strings.Replace(s,"?", "", -1)
    s = strings.Replace(s,"(", "", -1)
    s = strings.Replace(s,")", "", -1)
    s = strings.Replace(s,";", "", -1)
    s = strings.Replace(s,":", "", -1)
    s = strings.Replace(s,"[", "", -1)
    s = strings.Replace(s,"]", "", -1)

    fruits := strings.Split(s, " ")
    apples, _ := strconv.Atoi(fruits[0])
    oranges, _ := strconv.Atoi(fruits[1])

    return n - apples - oranges
}

