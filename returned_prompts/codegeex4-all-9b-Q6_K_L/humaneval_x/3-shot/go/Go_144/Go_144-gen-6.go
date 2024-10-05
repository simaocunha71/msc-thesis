    a,b := strings.Split(x,"/")
    c,d := strings.Split(n,"/")

    x1,_ := strconv.Atoi(a)
    y1,_ := strconv.Atoi(b)
    x2,_ := strconv.Atoi(c)
    y2,_ := strconv.Atoi(d)

    if (x1*y2)%y1 == 0 && (x2*y1)%y2 == 0 {
        return true
    }else{
        return false
    }
}



