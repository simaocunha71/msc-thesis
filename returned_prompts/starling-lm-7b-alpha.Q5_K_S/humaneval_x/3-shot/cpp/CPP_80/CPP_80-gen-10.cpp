    if (s.length()<3)
    return false;

    int i,j,k;
    char chr1,chr2,chr3;
    for (i=0;i<s.length()-2;i++)
    {
        chr1=s[i];
        chr2=s[i+1];
        chr3=s[i+2];
        if (chr1==chr2 || chr2==chr3 || chr1==chr3)
        return false;
    }
    return true;
}


