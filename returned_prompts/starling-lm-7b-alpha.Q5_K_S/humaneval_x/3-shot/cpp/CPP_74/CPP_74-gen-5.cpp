    int i;
    int counter1=0;
    int counter2=0;
    for (i=0;i<lst1.size();i++)
    counter1+=lst1[i].length();

    for (i=0;i<lst2.size();i++)
    counter2+=lst2[i].length();

    if (counter1<counter2)
    return lst1;
    else if (counter1>counter2)
    return lst2;
    else
    return lst1;
}



