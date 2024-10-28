    int i,count=0;
    for (i=0;i<n.size();i++)
    {
        int temp=abs(n[i]);
        int sum=0;
        while (temp>0){
        sum+=temp%10;
        temp/=10;
        }
        if (sum>0)
        count+=1;
    }
    return count;
}



