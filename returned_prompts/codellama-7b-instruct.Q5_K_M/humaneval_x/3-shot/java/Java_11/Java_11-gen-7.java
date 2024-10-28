        StringBuilder result = new StringBuilder();
        int a_index = a.length() - 1;
        int b_index = b.length() - 1;
        int carry = 0;

        while (a_index >= 0 || b_index >= 0 || carry == 1) {
            int a_bit = a_index >= 0 ? a.charAt(a_index) - '0' : 0;
            int b_bit = b_index >= 0 ? b.charAt(b_index) - '0' : 0;
            int sum = a_bit ^ b_bit ^ carry;

            result.append(sum);

            carry = a_bit & b_bit | a_bit & carry | b_bit & carry;

            a_index--;
            b_index--;
        }
        return result.reverse().toString();
    }
}

