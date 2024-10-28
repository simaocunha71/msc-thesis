    string binary;
    while(decimal>0)
    {
        binary=to_string(decimal%2)+binary;
        decimal=decimal/2;
    }
    return "db"+binary+"db";
} // this function will return a string of '0's and '1's with "db" at the start and end
// Note: this function is written for decimal_to_binary(int decimal) not float decimal


