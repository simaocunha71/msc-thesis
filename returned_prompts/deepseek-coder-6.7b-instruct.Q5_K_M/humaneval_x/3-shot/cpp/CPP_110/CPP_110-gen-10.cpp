    int odd_lst1 = 0;
    int odd_lst2 = 0;
    for (int i = 0; i < lst1.size(); i++)
    {
        if (lst1[i] % 2 != 0)
            odd_lst1++;
        if (lst2[i] % 2 != 0)
            odd_lst2++;
    }
    if (odd_lst1 > odd_lst2)
        return "NO";
    else
        return "YES";
}


