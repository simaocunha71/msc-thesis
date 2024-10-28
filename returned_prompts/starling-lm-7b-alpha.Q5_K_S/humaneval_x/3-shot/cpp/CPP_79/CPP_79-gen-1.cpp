    string binary="";
    int i;
    for (i=0;i<10;i++)
    {
    binary+=(decimal%2)+'0';
    decimal=decimal/2;
    }
    return "db"+binary+"db";
}

