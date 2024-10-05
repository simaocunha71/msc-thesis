    int i,sum=0;
    float temp;
    for (i=0;i<lst.size();i++)
    {
        temp=int(ceil(lst[i]));
        sum+=pow(temp,2);
    }
    return sum;
}



