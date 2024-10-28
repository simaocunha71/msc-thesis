public String decimalToBinary(int decimal) {
    String binary = Integer.toBinaryString(decimal);
    return "db" + binary + "db";
}
This solution works by using the built-in method Integer.toBinaryString() to convert the decimal number to a binary string. This method returns a string in which each binary digit is represented by a character. The resulting string is then prefixed and suffixed with "db" to match the expected output format. The function returns this final string.

The time complexity of this solution is O(1), because the conversion to binary string is a constant time operation. The space complexity is also O(1), because the size of the output string is proportional to the size of the input decimal number. However, in the worst case, the size of the output string can be at most 32 characters (for a 32-bit integer), so the space complexity is effectively constant.