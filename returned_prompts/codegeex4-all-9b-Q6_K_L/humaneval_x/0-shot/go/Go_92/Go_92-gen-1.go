func AnyInt(x, y, z interface{}) bool {
    return (x.(int)+y.(int)==z || x.(int)+z.(int)==y || y.(int)+z.(int)==x) && isInt(x) && isInt(y) && isInt(z)
}

func isInt(x interface{}) bool {
    _, ok := x.(int)
    return ok
}