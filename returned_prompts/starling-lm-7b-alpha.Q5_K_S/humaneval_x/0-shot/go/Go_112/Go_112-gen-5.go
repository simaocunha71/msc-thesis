    s2 := make([]byte,len(s))
    for i:=0;i<len(s);i++ {
        s2[i] = s[i]
    }
    i:=0
    j:=len(s)-1
    for ;i<j;i++ {
        for _,v := range c {
            if s2[i] == v {
                s2 = append(s2[:i], s2[i+1:]...)
                i--
                break
            }
        }
        for _,v := range c {
            if s2[j] == v {
                s2 = append(s2[:j], s2[j+1:]...)
                j--
                break
            }
        }
    }
    result := string(s2)
    if result == strings.Join(strings.Fields(result), "") {
        return [2]interface{}{result,true}
    } else {
        return [2]interface{}{result,false}
    }
}







































































































































































































































































