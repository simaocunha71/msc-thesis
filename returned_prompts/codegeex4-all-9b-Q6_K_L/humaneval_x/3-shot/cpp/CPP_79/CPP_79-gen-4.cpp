    string binary="";
    char c;
    while (decimal>0)
    {
        c='0'+(decimal%2);
        binary=c+binary;
        decimal/=2;
    }
    binary="db"+binary+"db";
    return binary;
}

