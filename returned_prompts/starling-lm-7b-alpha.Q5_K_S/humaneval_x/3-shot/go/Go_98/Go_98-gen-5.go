    result := 0
    for i:=0;i<len(s);i+=2{
        if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
            result += 1
        }
    }
    return result
}



