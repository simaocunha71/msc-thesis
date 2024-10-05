    int count=0, i=2;
    while(n>0){
        n-=i;
        if(n>=0 && n%2==0)
            count++;
        i+=2;
    }
    return count==4;
}

