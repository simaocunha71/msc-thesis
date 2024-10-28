    var max int
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
}  //or 
return math.MaxInt32
}  //or 
maxInt := int(math.MaxFloat64)
max := int64(0)
for _, v := range l {
    if int64(v) > maxInt {
        maxInt = int64(v)
    }
} 
return maxInt



