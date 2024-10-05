    for(int i=n-1; i>0; i--)
    {
        if(n%i==0)
        return i;
    }
    return 1;
}
//or
int largest_divisor(int n){
    for(int i=n/2; i>0; i--)
    {
        if(n%i==0)
        return i;
    }
    return 1;
}
//or
int largest_divisor(int n){
    for(int i=sqrt(n); i>0; i--)
    {
        if(n%i==0)
        return i;
    }
    return 1;
}
//or
int largest_divisor(int n){
    for(int i=n%2==0 ? n/2 : n-1; i>1; i--)
    {
        if(n%i==0)
        return i;
    }
    return 1;
}
//or
int largest_divisor(int n){
    for(int i=n; i>1; i--)
    {
        if(n%i==0)
        return i;
    }
    return 1;
}

