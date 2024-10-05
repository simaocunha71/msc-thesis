    string binary="";
    int i;
    for (i=0;i<10;i++)
    {
        if (decimal%2==0)
        binary+='0';
        else
        binary+='1';
        decimal/=2;
    }
    return "db"+binary+"db";
}



