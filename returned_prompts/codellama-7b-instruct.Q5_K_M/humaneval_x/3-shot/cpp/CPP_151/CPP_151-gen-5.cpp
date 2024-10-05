    long long sum=0;
    for(int i=0;i<lst.size();i++)
    {
        if(lst[i]>0&&(int)lst[i]==lst[i])
        sum+=(int)pow((double)lst[i],2);
    }
    return sum;
}


