    int i,j;
    int total_char_lst1=0;
    int total_char_lst2=0;
    for (i=0;i<lst1.size();i++)
    total_char_lst1+=lst1[i].length();
    for (j=0;j<lst2.size();j++)
    total_char_lst2+=lst2[j].length();
    if (total_char_lst1<total_char_lst2)
    return lst1;
    if (total_char_lst2<total_char_lst1)
    return lst2;
    return lst1;
}


