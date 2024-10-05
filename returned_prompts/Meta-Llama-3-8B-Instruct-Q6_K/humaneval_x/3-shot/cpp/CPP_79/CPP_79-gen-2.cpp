    string binary;
    while (decimal > 0) {
        if (decimal % 2 == 0)
            binary = "0" + binary;
        else
            binary = "1" + binary;
        decimal /= 2;
    }
    return "db" + binary + "db";
}
// OR
string decimal_to_binary(int decimal){
    return "db" + bitset<sizeof(int)*8>(decimal).to_string() + "db";
} // This one is more efficient and will work for larger inputs
// Since it uses bitset which directly converts integer to binary string
// Note: This solution assumes that the input integer is non-negative.
// If negative integers are also possible, you would need to handle them separately. 

