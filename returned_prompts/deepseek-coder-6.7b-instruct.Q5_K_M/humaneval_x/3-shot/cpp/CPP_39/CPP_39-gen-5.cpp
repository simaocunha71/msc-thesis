    int a=2;
    int b=3;
    int c;
    int count=2;
    if(n==1)
        return a;
    if(n==2)
        return b;
    for(int i=3;;i++){
        c=a+b;
        a=b;
        b=c;
        int flag=0;
        for(int j=2;j*j<=c;j++){
            if(c%j==0){
                flag=1;
                break;
            }
        }
        if(flag==0)
            count++;
        if(count==n)
            return c;
    }
}


