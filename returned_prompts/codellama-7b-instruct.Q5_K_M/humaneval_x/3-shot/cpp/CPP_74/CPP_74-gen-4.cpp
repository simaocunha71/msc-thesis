    int total_1=0;
    int total_2=0;
    for (int i=0;i<lst1.size();i++)
    total_1+=lst1[i].length();
    for (int i=0;i<lst2.size();i++)
    total_2+=lst2[i].length();
    if (total_1<total_2)
    return lst2;
    else if (total_1==total_2)
    return lst1;
    else
    return lst1;
}



