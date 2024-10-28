    if interval1[0] < interval2[0]{
        if interval1[1] > interval2[0]{
            if interval1[0] < interval2[1]{
                if interval1[1] > interval2[1]{
                    return "NO"
                }else{
                    return "YES"
                }
            }else{
                return "YES"
            }
        }else{
            return "NO"
        }
    }else{
        if interval1[0] < interval2[1]{
            if interval1[1] > interval2[1]{
                return "NO"
            }else{
                return "YES"
            }
        }else{
            return "NO"
        }
    }
}



