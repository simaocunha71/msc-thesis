    string binary;
    while (decimal>0)
    {
        binary=to_string(decimal%2)+binary;
        decimal/=2;
    }
    binary="db"+binary+"db";
    return binary;
}


