    int total1=0, total2=0;
    for (int i=0;i<lst1.size();i++)
    {
        total1+=lst1[i].size();
    }
    for (int i=0;i<lst2.size();i++)
    {
        total2+=lst2[i].size();
    }
    if (total1<total2)
        return lst1;
    else if (total1>total2)
        return lst2;
    else
        return lst1;
}  // return lst1 since lst1 is the first vector


