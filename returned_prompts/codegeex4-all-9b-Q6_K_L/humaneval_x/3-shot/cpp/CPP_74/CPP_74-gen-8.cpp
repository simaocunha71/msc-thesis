    int total1=0,total2=0;
    for (int i=0;i<lst1.size();i++)
    total1+=lst1[i].length();
    for (int i=0;i<lst2.size();i++)
    total2+=lst2[i].length();
    if (total1<=total2)
    return lst1;
    else
    return lst2;
}

