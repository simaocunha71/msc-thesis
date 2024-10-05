    var a,o,m int
    var t []string = strings.Split(s," ")
    for _,v := range t{
        if v=="apples"{
            a = 1
        }else if v=="oranges"{
            o = 1
        }else if v=="mango"{
            m = 1
        }
    }
    return n - a - o - m
}



