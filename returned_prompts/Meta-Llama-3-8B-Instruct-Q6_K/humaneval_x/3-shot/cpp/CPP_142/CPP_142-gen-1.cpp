    int sum=0;
    for (int i=0;i<lst.size();i++)
    {
        if ((i+1)%3==0 && (i+1)%4!=0)
        sum+=i*i;
        else if ((i+1)%4==0 && (i+1)%3!=0)
        sum+=i*i*i;
        else
        sum+=i;
    }
    return sum;
}  