    int i;
    int factor;
    for (i=n/2;i>1;i--){
        if (n%i==0){
            factor=i;
            while (n%factor==0)
            factor=factor/i;
            return factor;
        }
    }
    return 1;
}


