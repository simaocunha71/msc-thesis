    String binary = Integer.toBinaryString(decimal);
    return "db" + String.format("%32s", binary).replace(' ', '0') + "db";
}

Explanation:
The solution uses the built-in `Integer.toBinaryString()` method to convert the decimal number to a binary string. This method returns a string representing the binary representation of the given decimal number.

The `String.format()` method is used to pad the binary string with leading zeros to a minimum length of 32. This is done by specifying a format string of `%32s`, which means a string that is at least 32 characters long. If the string is shorter than 32 characters, it will be padded with spaces. The `replace(' ', '0')` method is then used to replace these spaces with zeros.

Finally, the "db" prefix and suffix are added to the binary string to match the required format. The resulting string is then returned.