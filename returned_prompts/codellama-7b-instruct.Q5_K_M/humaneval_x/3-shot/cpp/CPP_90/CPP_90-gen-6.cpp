    int a,b,i;
    a=lst[0];
    b=lst[1];
    if (b>a)
    return b;
    for (i=1;i<lst.size();i++)
    if (lst[i]<a)
    a=lst[i];
    return a;
}



