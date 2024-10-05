    int i;
    int total_apples=0;
    int total_oranges=0;
    int total_fruits=n;
    int total_mango=0;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='a')
        total_apples++;
        if (s[i]=='o')
        total_oranges++;
        if (s[i]==' ')
        total_fruits-=total_apples+total_oranges;
    }
    total_mango=total_fruits;
    return total_mango;
}


