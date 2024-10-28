        List<Integer> result = new ArrayList<>();
        // Ensure a is less than or equal to b
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }
        // Loop through all numbers from a to b
        for (int i = a; i <= b; i++) {
            // Convert the integer to a string
            String str = String.valueOf(i);
            // Check each digit in the string
            for (int j = 0; j < str.length(); j++) {
                // Check if the digit is even
                if ((str.charAt(j) - '0') % 2 == 0) {
                    result.add(i);
                    break; // Stop checking digits in this number
                }
            }
        }
        // Return the list of even digits
        return result;
    }
}
