    string binary;
    int r;
    while (decimal>0)
    {
        r=decimal%2;
        binary=char(r+48)+binary;
        decimal=decimal/2;
    }
    binary="db"+binary+"db";
    return binary;
}

