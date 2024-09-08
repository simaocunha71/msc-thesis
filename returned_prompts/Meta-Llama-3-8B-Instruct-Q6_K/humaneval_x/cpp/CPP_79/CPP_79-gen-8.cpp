    // Convert the decimal number to binary
    string binary;
    while(decimal > 0){
        binary = (decimal % 2 == 0 ? "0" : "1") + binary;
        decimal /= 2;
    }
    // Add "db" at the beginning and at the end of the string
    string result = "db" + binary + "db";
    return result;

}

int main()
{
    int decimal;
    cout<<"Enter the decimal number: ";
    cin>>decimal;
    cout << "The binary representation is: " << decimal_to_binary(decimal) << endl;
    return 0;
}
