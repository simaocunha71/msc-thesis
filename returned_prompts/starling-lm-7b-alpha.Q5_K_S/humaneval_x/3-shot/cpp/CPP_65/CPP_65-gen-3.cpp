    string digits;
    int i;
    for (i=0;i<x;i++)
    digits+=(x%10)+'0';
    if (shift>digits.length())
    {
        for (i=digits.length()-1;i>=0;i--)
        digits+=digits[i];
    }
    else
    {
        for (i=0;i<shift;i++)
        digits=digits.substr(1,digits.length()-1)+(digits[0]);
    }
    return digits;
}



