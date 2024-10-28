    int i;
    int counter1=0;
    int counter2=0;
    for (i=0;i<lst1.size();i++)
    if (lst1[i]%2==0)
    counter1+=1;
    for (i=0;i<lst2.size();i++)
    if (lst2[i]%2==0)
    counter2+=1;
    if (counter1+counter2<lst1.size())
    return "NO";
    return "YES";
}





