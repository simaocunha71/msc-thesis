    string digits;
    int i;
    for (i=0;i<x;i++)
    digits+=x%10+'0';
    x/=10;
    if (shift>digits.length())
    {
        for (i=0;i<digits.length();i++)
        digits+=digits[i];
        return digits.substr(digits.length()-shift,digits.length());
    }
    else
    {
        for (i=0;i<digits.length();i++)
        digits+=digits[i];
        return digits.substr(shift,digits.length()-shift);
    }
}


