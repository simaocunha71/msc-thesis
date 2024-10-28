    int sum=0;
    for (int i=0;i<lst.size();i++)
    {
        float num=ceil(lst[i]);
        sum+=pow(num,2);
    }
    return sum;
}