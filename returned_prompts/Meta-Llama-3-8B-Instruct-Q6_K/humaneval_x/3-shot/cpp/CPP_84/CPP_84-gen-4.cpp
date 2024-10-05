    int sum=0;
    int n=N;
    while(n>0)
    {
        int r=n%2;
        sum+=r;
        n=n/2;
    }
    string res="";
    while(sum>0)
    {
        if (sum%2==1)
            res='1'+res;
        else
            res='0'+res;
        sum=sum/2;
    }
    return res;
}
