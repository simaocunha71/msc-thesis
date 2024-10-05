    string binary;
    int i;
    for(i=0;i<8;i++)
    {
        int bit = decimal & 1;
        if(bit)
            binary = "1" + binary;
        else
            binary = "0" + binary;
        decimal >>= 1;
    }
    return "db" + binary + "db";
}
//OR
string decimal_to_binary(int decimal){
    return "db" + bitset<8>(decimal).to_string() + "db";
} 
// OR
string decimal_to_binary(int decimal){
    string binary = "";
    while(decimal > 0)
    {
        binary = (decimal & 1) ? "1" + binary : "0" + binary;
        decimal >>= 1;
    }
    return "db" + binary + "db";
} 
// OR
string decimal_to_binary(int decimal){
    string binary = "";
    while(decimal > 0)
    {
        binary = (decimal % 2 == 0)? "0" + binary : "1" + binary;
        decimal /= 2;
    }
    return "db" + binary + "db";
} 
// OR
string decimal_to_binary(int decimal){
    return "db" + to_binary(decimal) + "db";
}
string to_binary(int decimal){
    string binary = "";
    while(decimal > 0)
    {
        binary = (decimal % 2 == 0)? "0" + binary : "1" + binary;
        decimal /= 2;
    }
    return binary;
}  //OR
string decimal_to_binary(int decimal){
    ostringstream oss;
    oss << "db" << setfill('0') << binary << "db";
    return oss.str();
}
string binary = "";
while(decimal > 0)
{
    binary = (decimal % 2 == 0)? "0" + binary : "1" + binary;
    decimal /= 2;
} 
// OR
string decimal_to_binary(int decimal){
    string binary = "";
    while(decimal > 0)
    {
        binary = (decimal & 1) ? "1" + binary : "0" + binary;
        decimal >>= 1;
    }
    return "db" + binary + "db";
}
// OR
string decimal_to_binary(int decimal){
    string binary = "";
    while(decimal > 0)
    {
        binary = (decimal % 2 == 0)? "0"