    f,_ := strconv.ParseFloat(value,64)
    if f == float64(int(f)){
        return int(f)
    }else if f > float64(int(f)){
        return int(f)+1
    }else{
        return int(f)
    }
}



