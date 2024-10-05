    for (int i=0;i<lst1.size();i++)
    {
        for (int j=0;j<lst2.size();j++)
        {
            if (lst1[i]%2!=0)
            {
                int temp=lst1[i];
                lst1[i]=lst2[j];
                lst2[j]=temp;
                for (int k=0;k<lst1.size();k++)
                {
                    if (lst1[k]%2!=0)
                    {
                        return "YES";
                    }
                }
                for (int k=0;k<lst2.size();k++)
                {
                    lst1[i]=lst2[k];
                    for (int m=0;m<lst1.size();m++)
                    {
                        if (lst1[m]%2!=0)
                        {
                            return "YES";
                        }
                    }
                }
            }
        }
    }
    return "NO";
}
