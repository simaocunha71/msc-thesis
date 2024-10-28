    if n==0 || n==1{
        return 1
    }else{
        result := 1
        for i:=n; i>0; i--{
            result *= Factorial(i)
        }
        return result
    }
}

func Factorial(n int) int{
    if n<=1{
        return 1
    }
    return n*Factorial(n-1)
}



