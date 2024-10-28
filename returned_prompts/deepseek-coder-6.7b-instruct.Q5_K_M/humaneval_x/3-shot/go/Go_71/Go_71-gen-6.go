    if (a+b>c && b+c>a && c+a>b){
        p := (a+b+c)/2
        return math.Round((math.Sqrt(p*(p-a)*(p-b)*(p-c)))*100)/100
    }else{
        return -1
    }
}



