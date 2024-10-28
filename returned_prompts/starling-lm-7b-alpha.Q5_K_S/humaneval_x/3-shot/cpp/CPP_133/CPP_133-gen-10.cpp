    int i;
    float temp;
    int total=0;
    for (i=0;i<lst.size();i++)
    {
        temp=int(ceil(lst[i]));
        total+=temp*temp;
    }
    return total;
}



