    int i,j,count=0;
    for (i=1;i<=n;i++){
        for (j=1;j<=n;j++){
            if (i%10==1 || j%10==1)
            count++;
        }
    }
    return count;
}


