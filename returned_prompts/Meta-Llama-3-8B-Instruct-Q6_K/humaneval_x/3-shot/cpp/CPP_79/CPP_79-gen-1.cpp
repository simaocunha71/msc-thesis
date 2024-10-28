    string binary;
    binary += "db";
    while(decimal>0)
    {
        if (decimal%2==0)
        {
            binary += '0';
        }
        else
        {
            binary += '1';
        }
        decimal /= 2;
    }
    binary += "db";
    return binary;
}