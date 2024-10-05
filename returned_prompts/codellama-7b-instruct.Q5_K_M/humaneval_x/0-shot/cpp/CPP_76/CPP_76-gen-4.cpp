    if(n==1){
        return true;
    }
    if(x==1){
        return true;
    }
    if(x%n==0){
        return is_simple_power(x/n,n);
    }
    return false;
}
