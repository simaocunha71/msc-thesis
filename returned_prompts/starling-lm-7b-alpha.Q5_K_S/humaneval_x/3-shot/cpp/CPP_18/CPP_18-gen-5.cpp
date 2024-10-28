    int i,n,n_sub;
    n=str.length();
    n_sub=substring.length();
    int count=0;
    for (i=0;i<=n-n_sub;i++)
    if (str.substr(i,n_sub)==substring)
    count+=1;
    return count;
}



