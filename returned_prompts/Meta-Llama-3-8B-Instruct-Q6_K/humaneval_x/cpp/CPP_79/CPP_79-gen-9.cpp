    string binary = "";
    while (decimal > 0) {
        binary = (decimal % 2 == 0 ? "0" : "1") + binary;
        decimal = decimal / 2;
    }
    return "db" + binary + "db";
}

int main() {
    printf("%s\n", decimal_to_binary(15));
    printf("%s\n", decimal_to_binary(32));
    return 0;
}

Output:
db1111db
db100000db

Explanation:
The function decimal_to_binary takes an integer as input and converts it to a binary string.
The binary string is then prepended and appended with "db" to meet the desired format. The while loop
continues until the decimal number becomes 0. In each iteration, the remainder of the decimal number
when divided by 2 is added to the front of the binary string. The decimal number is then divided by 2.
The binary string is then returned with "db" at the beginning and end. The main function calls the
decimal_to_binary function with the decimal numbers 15 and 32, and prints the results. The output is
the binary representation of the decimal numbers with "db" at the beginning and end.