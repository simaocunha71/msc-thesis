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

int main() {
    printf("%s\n", decimal_to_binary(15));
    printf("%s\n", decimal_to_binary(32));
    return 0;
}