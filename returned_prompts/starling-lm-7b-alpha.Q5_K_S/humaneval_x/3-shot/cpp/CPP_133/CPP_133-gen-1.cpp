    int i;
    float temp;
    int sum=0;
    for (i=0;i<lst.size();i++)
    {
        temp=int(ceil(lst[i]));
        sum+=(temp*temp);
    }

    return sum;
}



