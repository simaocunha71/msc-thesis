    int i;
    int j;
    int k;
    int l;
    int total1=0;
    int total2=0;
    for (i=0;i<lst1.size();i++)
    {
        if (lst1[i]%2==0)
        total1+=1;
    }
    for (j=0;j<lst2.size();j++)
    {
        if (lst2[j]%2==0)
        total2+=1;
    }
    for (k=0;k<lst1.size();k++)
    {
        if (lst1[k]%2==1)
        {
            for (l=0;l<lst2.size();l++)
            {
                if (lst2[l]%2==0)
                {
                    if (total1+1==lst1.size())
                    return "YES";
                    if (total2+1==lst2.size())
                    return "YES";
                }
            }
        }
    }

    return "NO";
}

