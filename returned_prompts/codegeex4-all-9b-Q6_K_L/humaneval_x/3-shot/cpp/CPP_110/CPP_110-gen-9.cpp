    int i,j;
    int counter1=0,counter2=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==0)
    counter1+=1;
    for (j=0;j<lst2.size();j++)
    if (lst2[j]%2==0)
    counter2+=1;
    if (counter1==lst1.size() || counter2==lst2.size())
    return "YES";
    return "NO";
}

