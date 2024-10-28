    int count=0;
    int signed_sum=0;
    int i;
    for (i=0;i<n.size();i++)
    {
        signed_sum=0;
        while (n[i]!=0){
            signed_sum+=abs(n[i]%10);
            n[i]/=10;
        }
        if (signed_sum>0)
        count+=1;
    }
    return count;
}


