    int i,res=0;
    for (i=0;i<lst.size();i++)
    if (i%3==0)
    res+=lst[i]*lst[i];
    if (i%4==0 && i%3!=0)
    res+=lst[i]*lst[i]*lst[i];
    return res;
}



