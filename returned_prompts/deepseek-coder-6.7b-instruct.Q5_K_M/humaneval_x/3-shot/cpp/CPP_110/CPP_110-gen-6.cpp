    int i,j,c=0;
    for(i=0;i<lst1.size();i++)
    {
        if(lst1[i]%2==1)
        {
            for(j=0;j<lst2.size();j++)
            {
                if(lst2[j]%2==0)
                {
                    c++;
                    lst2[j]=lst1[i];
                    break;
                }
            }
        }
    }
    if(c==lst1.size()-i)
    return "YES";
    else
    return "NO";
}

