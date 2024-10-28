    int i,j,flag=0;
    for (i=0;i<lst1.size();i++)
    for (j=0;j<lst2.size();j++)
    if (lst1[i]%2!=0 && lst2[j]%2==0)
    {
    flag=1;
    swap(lst1[i],lst2[j]);
    }
    if (flag==0)
    return "NO";
    else
    return "YES";
}



