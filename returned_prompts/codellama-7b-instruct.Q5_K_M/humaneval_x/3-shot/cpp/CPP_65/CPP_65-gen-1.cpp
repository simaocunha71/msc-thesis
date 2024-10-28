    int digits[10];
    int i;
    string str;
    if (shift > 10)
    shift=10-shift;
    for (i=1;i<10;i++)
    digits[i]=i;
    for (i=0;i<shift;i++)
    {
        int temp=digits[1];
        for (int j=1;j<10;j++)
        digits[j]=digits[j+1];
        digits[10]=temp;
    }
    for (i=1;i<10;i++)
    str+=to_string(digits[i]);
    return str;
}



