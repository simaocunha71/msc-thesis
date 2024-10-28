    int len1=0,len2=0;
    int i;
    for (i=0;i<lst1.size();i++)
    len1+=lst1[i].length();
    for (i=0;i<lst2.size();i++)
    len2+=lst2[i].length();

    if (len1<len2)
    return lst1;
    else
    return lst2;
}

