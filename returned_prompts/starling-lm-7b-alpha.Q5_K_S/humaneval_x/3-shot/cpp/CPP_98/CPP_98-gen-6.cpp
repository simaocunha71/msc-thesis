    int count=0;
    char vowel[]={'A','E','I','O','U'};
    int i,j;
    for (i=0;i<s.length();i++)
    {
        if (i%2==0)
        for (j=0;j<5;j++)
        if (s[i]==vowel[j])
        count+=1;
    }
    return count;
}


