    if n==1 {
        return 1
    }
    if n==2 {
        return 2
    }

    var ones_count int = 0
    for i:=1; i<=(math.Pow(10,float64(n-2))); i++{
        if (i%10==1) || (math.Mod(i,10)==1){
            ones_count += 1
        }
    }
    return ones_count
}



