    int i,result=0;
    int lst_size=lst.size();
    for (i=0;i<lst_size;i++)
    if (i%2==0&&lst[i]%2==0)
    result+=lst[i];

    return result;
}



