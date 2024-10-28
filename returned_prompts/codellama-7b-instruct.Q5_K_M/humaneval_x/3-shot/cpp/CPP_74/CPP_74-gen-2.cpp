    int i,j;
    int total_chars_lst1=0;
    int total_chars_lst2=0;

    for (i=0;i<lst1.size();i++)
    total_chars_lst1+=lst1[i].length();

    for (j=0;j<lst2.size();j++)
    total_chars_lst2+=lst2[j].length();

    if (total_chars_lst1<total_chars_lst2)
    return lst1;
    else if (total_chars_lst1>total_chars_lst2)
    return lst2;
    else
    return lst1;
}






