    vector<int> all_integers;
    int level=0;
    char chr;
    int i;
    for (i=a;i<=b;i++)
    {
        chr=i;
        if (chr%2==0)
        all_integers.push_back(chr);
    }
    return all_integers;
}


