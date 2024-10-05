    var count int = 0
    for i := 0; i < len(str); i++{
        if len(str[i:]) < len(substring){
            break
        }

        if str[i:i+len(substring)] == substring {
            count += 1
            i += len(substring) - 1
        }
    }
    return count
}



