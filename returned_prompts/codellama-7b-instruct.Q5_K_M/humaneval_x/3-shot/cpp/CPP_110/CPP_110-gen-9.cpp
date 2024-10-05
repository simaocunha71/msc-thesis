    int i;
    int j;
    for (i=0;i<lst1.size();i++)
    for (j=0;j<lst2.size();j++)
    if (lst1[i]%2==0 && lst2[j]%2==0)
    if (lst1[i]==lst2[j])
    {
        lst1[i]=lst1[i]/2;
        lst2[j]=lst2[j]/2;
        i=lst1.size();
        j=lst2.size();
    }
    if (lst1[0]%2==0) return "YES";
    return "NO";
}


