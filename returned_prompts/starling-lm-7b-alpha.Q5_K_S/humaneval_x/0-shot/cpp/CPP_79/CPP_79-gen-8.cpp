    if(decimal == 0)
    {
        string result = "db0db";
        return result;
    }
    else if(decimal < 0)
    {
        string result = "db";
        decimal = -decimal;
        result += binary_to_decimal(decimal);
        result += "db";
        return result;
    }
    else if(decimal > 0)
    {
        string result = "db";
        result += binary_to_decimal(decimal);
        result += "db";
        return result;
    }
    else if(decimal == -1)
    {
        string result = "db";
        result += binary_to_decimal(decimal);
        result += "db";
        return result;
    }

    return "error";
}

string binary_to_decimal(int decimal){
    int binary_number = decimal;
    int remainder = 0;
    int binary_base = 1;
    int binary_decimal = 0;
    while(binary_number != 0)
    {
        remainder = binary_number % 2;
        binary_number = binary_number / 2;
        binary_decimal += remainder * binary_base;
        binary_base *= 10;
    }
    return to_string(binary_decimal);
}

int main()
{
    int decimal;
    cin>>decimal;
    cout<<decimal_to_binary(decimal);
}





























*/




















































































































