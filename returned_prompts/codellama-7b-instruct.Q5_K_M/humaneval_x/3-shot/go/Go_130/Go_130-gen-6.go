    if n==0{
        return []float64{1}
    }
    if n==1{
        return []float64{1,3}
    }
    if n==2{
        return []float64{1,3,2,8}
    }

    var result []float64 = []float64{1,3,2,8}

    for i := 3; i < n; i++ {
        if i%2==0{
            result = append(result, 1 + float64(i)/2)
        }else {
            var new_tri float64 = result[i-1] + result[i-2] + result[i+1]
            result = append(result, new_tri)
        }
    }
    return result
}



