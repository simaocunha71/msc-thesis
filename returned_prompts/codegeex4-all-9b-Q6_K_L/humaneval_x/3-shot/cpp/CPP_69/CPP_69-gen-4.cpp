    int max=-1;
    for (int i=0;i<lst.size();i++)
    {
        int temp=lst[i];
        int count=0;
        for (int j=0;j<lst.size();j++)
        {
            if (lst[j]==temp)
            count+=1;
        }
        if (count>=temp && temp>max)
            max=temp;
    }
    return max;
}

