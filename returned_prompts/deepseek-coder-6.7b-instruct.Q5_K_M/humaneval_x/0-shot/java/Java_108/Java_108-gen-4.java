        int count = 0;

        for (int num : arr) {
            int sum = 0;
            String numStr = Integer.toString(num);

            for (int i = 0; i < numStr.length(); i++) {
                char ch = numStr.charAt(i);
                if (ch == '-') {
                    continue;
                }
                sum += Character.getNumericValue(ch);
            }

            if (sum > 0) {
                count++;
            }
        }

        return count;
    }
}

This function works by first converting each integer in the array to a string. Then for each character in the string, it converts the character back to an integer and adds it to a sum. If the sum is greater than 0, it increments a counter. At the end, it returns the counter.

Also, this function assumes that the input list contains only integers. If the input list can contain non-integer elements, the function should be modified to handle this case.
