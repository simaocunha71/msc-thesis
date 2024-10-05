    string binary="";
    int number=decimal;
    while (number>0)
    {
        binary=(char)(number%2+'0')+binary;
        number=number/2;
    }
    binary="db"+binary+"db";
    return binary;
}

