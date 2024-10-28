    int lst1_total_char=0;
    int lst2_total_char=0;
    for (int i=0;i<lst1.size();i++)
    lst1_total_char+=lst1[i].length();
    for (int i=0;i<lst2.size();i++)
    lst2_total_char+=lst2[i].length();
    if (lst1_total_char>lst2_total_char)
    return lst2;
    return lst1;
}


