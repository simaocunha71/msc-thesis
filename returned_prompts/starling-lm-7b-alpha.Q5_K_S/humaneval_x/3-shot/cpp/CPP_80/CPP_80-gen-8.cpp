    if (s.length()<3) return false;
    int i;
    char chr;
    int count;
    for (i=0;i<s.length()-2;i++)
    {
        chr=s[i];
        count=0;
        while (i<s.length()-2 && chr==s[i+1] && chr==s[i+2])
        {
            count+=1;
            i+=1;
        }
        if (count>0)
        return false;
    }
    return true;
}



