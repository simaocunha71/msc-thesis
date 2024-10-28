public String decimalToBinary(int decimal) {
    StringBuilder binary = new StringBuilder();
    binary.append("db");

    while (decimal > 0) {
        int remainder = decimal % 2;
        decimal = decimal / 2;
        binary.append((remainder == 0) ? "0" : "1");
    }

    binary.append("db");
    return binary.toString();
}
