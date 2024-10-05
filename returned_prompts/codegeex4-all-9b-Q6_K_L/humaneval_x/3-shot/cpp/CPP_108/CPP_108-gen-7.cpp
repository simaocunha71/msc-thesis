    int i,j;
    int sum;
    int count=0;
    for (i=0;i<n.size();i++)
    {
        sum=0;
        if (n[i]>=0){
            while (n[i]>0){
                sum+=n[i]%10;
                n[i]/=10;
            }
        }
        if (n[i]<0){
            n[i]*=-1;
            while (n[i]>0){
                sum+=n[i]%10;
                n[i]/=10;
            }
            sum*=-1;
        }
        if (sum>0) count+=1;
    }
    return count;
}