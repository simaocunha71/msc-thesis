    int i,j;
    for(i=0;i<lst.size();i++)
    {
        int count=0;
        for(j=0;j<lst.size();j++)
        {
            if(lst[i]==lst[j])
            count++;
        }
        if(count>=lst[i])
        return lst[i];
    }
    return -1;
}

