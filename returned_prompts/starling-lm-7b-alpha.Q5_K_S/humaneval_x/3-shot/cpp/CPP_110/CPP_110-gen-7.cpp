    int i;
    int c=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==0)
    c+=1;

    if (c==lst1.size()) return "NO";

    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==1)
    if (binary_search(lst2.begin(),lst2.end(),lst1[i]))
    {
        int j;
        for (j=0;j<lst2.size();j++)
        if (lst2[j]==lst1[i])
        {
            lst2[j]=0;
            break;
        }
    }

    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==1) return "NO";

    return "YES";
}




