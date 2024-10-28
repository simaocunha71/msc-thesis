    if(n<=1) return 0;
    if(n==2) return 1;
    int count=0;
    for(int i=10;i<=90;i++){
        if(i%10==1)count++;
    }
    return count;


