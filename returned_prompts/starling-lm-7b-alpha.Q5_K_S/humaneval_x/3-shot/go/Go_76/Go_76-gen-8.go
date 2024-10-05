    for i:=0;i<32;i++{
        if n==1{
            return x==1
        }
        if n==2{
            if x==1||x==2{
                return true
            }
            return false
        }
        if n==3{
            if x==1||x==3||x==9{
                return true
            }
            return false
        }
        if n==4{
            if x==1||x==4{
                return true
            }
            return false
        }
        if n==5{
            if x==1||x==5{
                return true
            }
            return false
        }
        if n==6{
            if x==1||x==3||x==6{
                return true
            }
            return false
        }
        if n==7{
            if x==1||x==7{
                return true
            }
            return false
        }
        if n==8{
            if x==1||x==8{
                return true
            }
            return false
        }
        if n==9{
            if x==1||x==3||x==9{
                return true
            }
            return false
        }
    }
    return false
}



