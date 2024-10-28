    string binary_string;
    int binary_num=0;
    while (decimal>0)
    {
        binary_num=decimal%2;
        binary_string=to_string(binary_num)+binary_string;
        decimal/=2;
    }
    binary_string="db"+binary_string+"db";
    return binary_string;
}


