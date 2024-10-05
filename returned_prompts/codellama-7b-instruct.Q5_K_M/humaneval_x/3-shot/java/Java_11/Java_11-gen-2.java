        StringBuilder result = new StringBuilder();
        int carry = 0;

        for (int i = 0; i < a.length(); i++) {
            int xor = (a.charAt(i) == '1') ^ (b.charAt(i) == '1') ^ carry;
            carry = xor == 1 ? 1 : 0;
            result.append(xor == 1 ? "1" : "0");
        }
        return result.toString();

    }
}

