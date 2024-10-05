    int i;
    int length1=0,length2=0;
    for (i=0;i<lst1.size();i++)
    length1+=lst1[i].length();
    for (i=0;i<lst2.size();i++)
    length2+=lst2[i].length();
    if (length1<=length2)
    return lst1;
    else
    return lst2;
}

