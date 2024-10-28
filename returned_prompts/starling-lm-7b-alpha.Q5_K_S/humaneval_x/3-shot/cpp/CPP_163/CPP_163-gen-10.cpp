    vector<int> all_integers;
    int chr;
    int level=0;
    char chr1;
    char chr2;
    int i;
    for (i=a;i<=b;i++)
    {
        chr=i;
        chr1=chr%10;
        chr2=chr/10;
        if (chr1%2==0)
        {
        all_integers.push_back(i);
        }
        i=chr2;
    }
    return all_integers;
}


