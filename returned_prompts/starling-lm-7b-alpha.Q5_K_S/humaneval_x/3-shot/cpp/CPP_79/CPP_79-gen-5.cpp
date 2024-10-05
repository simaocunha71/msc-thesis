    string binary_str;
    string temp_str;
    int i;
    char chr;
    for (i=0;i<16;i++)
    {
        chr=(decimal/pow(2,i))%2;
        temp_str+=chr;
    }
    binary_str="db"+temp_str+"db";
    return binary_str;
}



