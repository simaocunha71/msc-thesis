    result := make([]rune,0)
    for _,r := range s {
        if !strings.Contains(c,string(r)){
            result = append(result,r)
        }
    }
    if strings.EqualFold(string(result),string(reverse(result))) {
        return [2]interface{}{string(result),true}
    }
    return [2]interface{}{string(result),false}
}

func reverse(s []rune) []rune{
    for i,j:=0,len(s)-1;i<j;i,j=i+1,j-1{
        s[i],s[j]=s[j],s[i]
    }
    return s
}



