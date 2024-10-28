    string binary="db";
    int a;
    while (decimal>0)
    {
        a=decimal%2;
        binary+=a;
        decimal=decimal/2;
    }
    binary+="db";
    return binary;
}

