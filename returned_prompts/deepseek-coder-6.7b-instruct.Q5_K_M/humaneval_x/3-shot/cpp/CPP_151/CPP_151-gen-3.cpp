    long long sum=0;
    for(int i=0;i<lst.size();i++)
        if(lst[i]>0 && floor(lst[i])==lst[i] && int(lst[i])%2==1)
            sum+=pow(lst[i],2);
    return sum;
}


