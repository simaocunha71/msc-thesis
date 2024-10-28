    if x == y+z || y == x+z || z == x+y{
        if isInt(x) && isInt(y) && isInt(z){
            return true
        }
    }
    return false
}

func isInt(x interface{}) bool {
    _,ok := x.(int)
    return ok
}



