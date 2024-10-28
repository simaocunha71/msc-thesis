    string binary = "";
    while(decimal > 0) {
        binary = to_string(decimal % 2) + binary;
        decimal /= 2;
    }
    return "db" + binary + "db";
}


A: You have to use the modulo operator to get the remainder of division by 2 and concatenate the result to the binary string. Then divide the decimal by 2 to get the next digit. Repeat until the decimal is 0.
Finally, add the "db" at the beginning and at the end of the binary string.

A: You should use the modulo operator to get the remainder of division by 2 and prepend the result to the binary string. Then divide the decimal by 2 to get the next digit. Repeat until the decimal is 0.
Finally, add the "db" at the beginning and at the end of the binary string.

A: You can use the modulo operator to get the remainder of division by 2 and append it to the binary string. Then divide the decimal by 2 to get the next digit. Repeat until the decimal is 0.
Finally, add the "db" at the beginning and at the end of the binary string.

A: You can use the modulo operator to get the remainder of division by 2 and prepend it to the binary string. Then divide the decimal by 2 to get the next digit. Repeat until the decimal is 0.
Finally, add the "db" at the beginning and at the end of the binary string.

A: You can use the modulo operator to get the remainder of division by 2 and append it to the binary string. Then divide the decimal by 2 to get the next digit. Repeat until the decimal is 0.
Finally, add the "db" at the beginning and at the end of the binary string.

A: You can use the modulo operator to get the remainder of division by 2 and prepend it to the binary string. Then divide the decimal by 2 to get the next digit. Repeat until the decimal is 0.
Finally, add the "db" at the beginning and at the end of the binary string.

A: You can use the modulo operator to get the remainder of division by 2 and append it to the binary string.