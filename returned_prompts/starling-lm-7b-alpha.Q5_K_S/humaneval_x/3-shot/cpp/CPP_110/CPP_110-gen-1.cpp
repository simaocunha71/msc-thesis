    int i;
    int even_count=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==0)
        even_count+=1;

    if (even_count==lst1.size())
        return "YES";

    for (i=0;i<lst2.size();i++)
    {
        if (lst2[i]%2==0)
        {
            lst1[i]=lst2[i];
            break;
        }
    }

    if (i==lst2.size())
        return "NO";

    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2!=0)
    {
        for (int j=i+1;j<lst2.size();j++)
        {
            if (lst2[j]%2==0)
            {
                lst1[i]=lst2[j];
                lst2[j]=lst1[i];
                break;
            }
        }
    }

    return "YES";
}



