        // Convert the integer to binary
        String binary = Integer.toBinaryString(N);

        // Initialize sum to 0
        int sum = 0;

        // Iterate over each digit in the binary number
        for(int i = 0; i < binary.length(); i++) {

            // If the digit is a '1', add 1 to sum
            if(binary.charAt(i) == '1') {
                sum++;
            }
        }

        // Convert sum to binary and return
        return Integer.toBinaryString(sum);
    }
}

Test cases:
    Input: 1000
    Output: "1"
    Explanation: The sum of the digits in 1000 is 1.

    Input: 150
    Output: "110"
    Explanation: The sum of the digits in 150 is 6 which in binary is 110.

    Input: 147
    Output: "1100"
    Explanation: The sum of the digits in 147 is 12 which in binary is 1100.
 */






































































































































































































































