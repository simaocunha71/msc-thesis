    string digits;
    int i,digit;
    for (i=0;i<shift;i++)
    {
        digit=x%10;
        x/=10;
        digits+=to_string(digit);
    }
    while (x!=0){
        digit=x%10;
        x/=10;
        digits+=to_string(digit);
    }
    if (digits.length()<shift)
    {
        for (i=0;i<digits.length();i++)
        digits+=digits[digits.length()-i-1];
    }
    return digits;
}



