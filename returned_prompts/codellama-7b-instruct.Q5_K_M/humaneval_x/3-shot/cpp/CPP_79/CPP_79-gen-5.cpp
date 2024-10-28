    string binary_string = "db";
    while (decimal>0)
    {
        binary_string+= (decimal%2==0) ? '0' : '1';
        decimal/=2;
    }
    return binary_string+"db";
}


