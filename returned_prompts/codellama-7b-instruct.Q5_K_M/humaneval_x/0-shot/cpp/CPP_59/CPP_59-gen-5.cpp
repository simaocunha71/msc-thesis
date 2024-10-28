    for(int i=2;i<=n;i++){
        if(n%i==0){
            n=i;
            goto A;
        }
    }
    return n;
}

