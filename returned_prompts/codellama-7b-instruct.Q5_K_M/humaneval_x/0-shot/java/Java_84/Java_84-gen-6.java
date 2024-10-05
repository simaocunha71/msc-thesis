        // check if number is in binary
        if (N < 2) {
            return "0";
        }
        if (N == 2) {
            return "10";
        }
        // convert number to binary
        String binary = Integer.toBinaryString(N);
        // sum digits
        int sum = 0;
        for (int i = 0; i < binary.length(); i++) {
            sum += Character.getNumericValue(binary.charAt(i));
        }
        // check for leading zeroes
        while (binary.length() > 1 && binary.charAt(0) == '0') {
            binary = binary.substring(1);
        }
        // return sum
        return Integer.toBinaryString(sum);
    }
}