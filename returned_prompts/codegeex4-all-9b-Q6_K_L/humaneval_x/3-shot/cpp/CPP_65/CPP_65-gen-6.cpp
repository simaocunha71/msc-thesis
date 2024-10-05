    string digits=to_string(x);
    int l=digits.length();
    if (shift>l)
    {
        string reverse="";
        for (int i=l-1;i>=0;i--)
        reverse+=digits[i];
        return reverse;
    }
    string shifted="";
    for (int i=shift;i<l;i++)
    shifted+=digits[i];
    for (int i=0;i<shift;i++)
    shifted+=digits[i];
    return shifted;
}

