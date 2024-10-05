    int i,j;
    int even1=0,odd1=0,even2=0,odd2=0;
    for (i=0;i<lst1.size();i++)
    {
        if (lst1[i]%2==0)
            even1+=1;
        else
            odd1+=1;
    }
    for (i=0;i<lst2.size();i++)
    {
        if (lst2[i]%2==0)
            even2+=1;
        else
            odd2+=1;
    }
    if (odd1<=even2)
        return "YES";
    return "NO";
}

