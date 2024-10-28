    int i,sum=0;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr>='A' && chr<='Z') sum+=chr-'A'+1;
    }
    return sum;
}



