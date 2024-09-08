    // Convert the decimal number to binary
    string binary = "";
    while(decimal > 0){
        binary = (decimal % 2 == 0 ? "0" : "1") + binary;
        decimal /= 2;
    }

    // Add the extra characters to the binary string
    binary = "db" + binary + "db";
    return binary;

}

int main()
{
    int decimal;
    printf("Enter a decimal number: ");
    scanf("%d", &decimal);
    printf("The binary representation of %d is: %s\n", decimal, decimal_to_binary(decimal));
    return 0;
}

