    for (int i=0;i<lst1.size();i++)
    {
        for (int j=0;j<lst2.size();j++)
        {
            if (lst1[i]%2!=0)
            {
                if (lst2[j]%2==0)
                {
                    int temp=lst1[i];
                    lst1[i]=lst2[j];
                    lst2[j]=temp;
                }
            }
        }
    }
    for (int i=0;i<lst1.size();i++)
    {
        if (lst1[i]%2!=0)
        {
            return "NO";
        }
    }
    return "YES";
}