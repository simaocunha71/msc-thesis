    int i,j;
    int count1=0,count2=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==0)
    count1+=1;
    for (j=0;j<lst2.size();j++)
    if (lst2[j]%2==0)
    count2+=1;

    if (count1==lst1.size())
    return "NO";
    if (count2>=lst1.size()-count1)
    return "YES";
    else
    return "NO";
}



