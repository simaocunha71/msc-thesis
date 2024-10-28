    int r;
    r = 1;
    while (n>0){
        if (n%2==1)
        r=r*r%p;
        n/=2;
        r=r*r%p;
    }
    return r;
}



