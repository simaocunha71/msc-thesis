    int i;
    int count=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==0)
    count+=1;
    if (count==lst1.size())
    return "YES";
    else{
        count=0;
        for (i=0;i<lst2.size();i++)
        if (lst2[i]%2==0)
        count+=1;
        if (count==lst2.size())
        return "YES";
        else
        return "NO";
    }
}

