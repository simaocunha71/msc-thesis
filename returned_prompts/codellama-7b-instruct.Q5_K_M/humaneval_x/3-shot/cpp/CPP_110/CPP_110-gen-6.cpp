    bool can_exchange = true;
    for (int i=0;i<lst1.size();i++)
    if (lst1[i]%2!=0)
    can_exchange=false;
    for (int i=0;i<lst2.size();i++)
    if (lst2[i]%2!=0)
    can_exchange=false;
    return can_exchange ? "YES" : "NO";
}


