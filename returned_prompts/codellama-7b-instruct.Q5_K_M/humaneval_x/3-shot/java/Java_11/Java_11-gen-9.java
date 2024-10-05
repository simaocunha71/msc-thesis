        StringBuilder result = new StringBuilder();
        int carry = 0;
        int a_index = a.length() - 1;
        int b_index = b.length() - 1;

        while (a_index >= 0 && b_index >= 0) {
            int a_bit = a.charAt(a_index) - '0';
            int b_bit = b.charAt(b_index) - '0';
            int xor_bit = a_bit ^ b_bit;

            if (xor_bit == 1) {
                carry = 1;
            }

            result.insert(0, "" + carry);
            carry = a_bit & b_bit;

            a_index--;
            b_index--;
        }

        while (a_index >= 0) {
            int a_bit = a.charAt(a_index) - '0';

            if (carry == 1 && a_bit == 1) {
                result.insert(0, "1");
            } else {
                result.insert(0, "0");
            }

            a_index--;
        }

        while (b_index >= 0) {
            int b_bit = b.charAt(b_index) - '0';

            if (carry == 1 && b_bit == 1) {
                result.insert(0, "1");
            } else {
                result.insert(0, "0");
            }

            b_index--;
        }

        return result.toString();
    }
}

