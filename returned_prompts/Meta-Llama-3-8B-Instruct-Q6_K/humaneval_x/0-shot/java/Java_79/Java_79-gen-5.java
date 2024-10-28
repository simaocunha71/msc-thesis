        // Your code goes here
        String binary = Integer.toBinaryString(decimal);
        return "db" + binary + "db";
    }
}

Explanation:
This solution uses the built-in `Integer.toBinaryString()` method in Java to convert the decimal number to binary. The method returns a string representation of the binary number.

The extra characters 'db' are added to the beginning and end of the binary string as per the problem statement.

The `decimalToBinary()` method takes an integer as input, converts it to binary using `Integer.toBinaryString()`, and then returns a string that starts with 'db', followed by the binary string, and ends with 'db'. This ensures that the output matches the format specified in the problem statement.