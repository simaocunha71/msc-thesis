    result := strings.ReplaceAll(s,"", "")
    if result == strings.Join([]rune(result)[len(result)/2:], "")[::-1] {
        return [2]interface{}{result,true}
    }else{
        return [2]interface{}{result,false}
    }
}




