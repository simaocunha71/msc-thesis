    int i;
    int size1=0,size2=0;
    for (i=0;i<lst1.size();i++)
    size1+=lst1[i].length();
    for (i=0;i<lst2.size();i++)
    size2+=lst2[i].length();

    if (size1<size2)
    return lst1;
    if (size1>size2)
    return lst2;
    return lst1;
}


