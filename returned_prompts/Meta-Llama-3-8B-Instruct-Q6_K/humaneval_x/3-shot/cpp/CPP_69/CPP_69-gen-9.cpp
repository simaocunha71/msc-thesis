    int max=0;
    int res=-1;
    for (int i=1;i<=lst.size();i++)
    {
        int count=0;
        for (int j=0;j<lst.size();j++)
        {
            if (lst[j]==i)
                count++;
        }
        if (count>=i && i>max)
        {
            max=i;
            res=i;
        }
    }
    return res;
}