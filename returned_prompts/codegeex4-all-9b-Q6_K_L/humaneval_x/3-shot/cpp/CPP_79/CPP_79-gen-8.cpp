    string binary="";
    while (decimal>0)
    {
        int digit=decimal%2;
        binary=to_string(digit)+binary;
        decimal=decimal/2;
    }
    return "db"+binary+"db";
}

