    s = strings.Replace(s,"apples"," ",-1)
    s = strings.Replace(s,"oranges"," ",-1)
    s = strings.Replace(s,"and"," ",-1)
    s = strings.Replace(s," ","", -1)
    num1,_ := strconv.Atoi(s)

    return n-num1
}

