    string binary = "db";
    while (decimal > 0) {
        binary = (decimal % 2 == 0 ? "0" : "1") + binary;
        decimal /= 2;
    }
    binary += "db";
    return binary;
} // End of function decimal_to_binary. 
