    int i,cnt=0;
    for (i=1;i<n;i++)
    if ((i%11==0)||(i%13==0))
    if (i%10==7)
    cnt+=1;
    return cnt;
}


