    int sum;
    int count=0;
    for(int i=0;i<n.size();i++)
    {
        sum=0;
        while(n[i]){
            sum+=n[i]%10;
            n[i]/=10;
        }
        if(sum>0)
        count++;
    }
    return count;
}


