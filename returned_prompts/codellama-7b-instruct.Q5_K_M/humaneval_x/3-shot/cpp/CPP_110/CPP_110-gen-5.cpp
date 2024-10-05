    int i;
    int is_even=0;
    for (i=0;i<lst1.size();i++)
    {
        if (lst1[i]%2==0)
        is_even+=1;
    }
    if (is_even==lst1.size())
    return "YES";
    else
    return "NO";
}


