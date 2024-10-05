    int i,s;
    int res=0;
    for (i=0;i<n.size();i++)
    {
        s=0;
        while (n[i]!=0){
        s+=abs(n[i]%10);
        n[i]/=10;
        }
        if (s>0) res+=1;
    }
    return res;
}



