    float sum=0;
    for (int i=0;i<lst.size();i++)
    {
        float a=ceil(lst[i]);
        sum+=pow(a,2);
    }
    return (int)sum;
}