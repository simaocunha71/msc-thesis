    string binary;
    binary="db";
    int i;
    for (i=decimal;i>0;i>>=1)
    {
        binary=(i&1)?"1":"0";
    }
    binary="db"+binary+"db";
    return binary;
}
// or
string decimal_to_binary(int decimal){
    string binary;
    binary="db";
    while(decimal>0)
    {
        binary=(decimal&1)?"1":"0";
        decimal>>=1;
    }
    binary="db"+binary+"db";
    return binary;
} 

