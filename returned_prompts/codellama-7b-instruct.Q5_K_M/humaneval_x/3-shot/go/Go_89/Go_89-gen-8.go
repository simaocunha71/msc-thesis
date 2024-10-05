    result := make([]rune, 0)
    for _, c := range s{
        if c >= 'a' && c <= 'z'{
            result = append(result, (c+2*2-'a'+'a')%26 + 'a' -1)
        }else if c >= 'A' && c <= 'Z'{
            result = append(result, (c+2*2-'A'+'A')%26 + 'A' -1)
        }else{
            result = append(result, c)
        }
    }
    return string(result)
}


