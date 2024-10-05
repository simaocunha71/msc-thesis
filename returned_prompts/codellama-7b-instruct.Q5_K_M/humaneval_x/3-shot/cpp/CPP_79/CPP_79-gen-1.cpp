    string binary;
    int i;
    for (i=0;i<16;i++)
    {
        if (decimal>=pow(2,i))
        {
            binary.push_back('1');
            decimal-=pow(2,i);
        }
        else
        binary.push_back('0');
    }
    binary.insert(0,"db");
    binary.push_back("db");
    return binary;
}


