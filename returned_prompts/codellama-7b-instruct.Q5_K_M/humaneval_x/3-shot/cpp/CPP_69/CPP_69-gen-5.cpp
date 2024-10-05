    int i;
    int temp=0;
    int max=0;
    int counter;
    for (i=0;i<lst.size();i++)
    {
        counter=0;
        temp=lst[i];
        for (int j=0;j<lst.size();j++)
        {
            if (temp==lst[j])
            counter+=1;
        }
        if (counter>=temp && temp>max)
        max=temp;
    }
    if (max>0)
    return max;
    else
    return -1;
}


