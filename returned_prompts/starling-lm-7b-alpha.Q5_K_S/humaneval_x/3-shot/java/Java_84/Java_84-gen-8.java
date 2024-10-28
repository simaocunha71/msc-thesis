        String result = "";
        int carry = 0;
        while (N != 0) {
            result = (result + Integer.toBinaryString(N & 1)) + result;
            carry = N >> 1;
            N = carry;
        }
        return result;
    }
}

