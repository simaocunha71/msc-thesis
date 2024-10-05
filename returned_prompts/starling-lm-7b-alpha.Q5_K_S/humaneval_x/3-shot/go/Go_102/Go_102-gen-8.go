    if x%2==0 && x<=y{
        return x
    }else if (y%2==0 && y>=x){
        return y
    }else if x%2==1 && y%2==0 && x<=y{
        return x+1
    }else if (x%2==0 && y%2==1 && y>=x){
        return y-1
    }else{
        return -1
    }
}



