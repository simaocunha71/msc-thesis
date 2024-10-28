    result := strings.Replace(s,"","",-1)
    if result == strings.Join([]rune(result)[len(result)/2:], "") {
        return [2]interface{}{result,true}
    }else{
        return [2]interface{}{result,false}
    }
}



