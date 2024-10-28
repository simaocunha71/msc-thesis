    int odd1 = 0;
    int odd2 = 0;
    for(int i = 0; i < lst1.size(); i++)
    {
        if(lst1[i] % 2 != 0)
            odd1++;
        if(lst2[i] % 2 != 0)
            odd2++;
    }
    if(odd1 == odd2)
        return "YES";
    else
        return "NO";
}

