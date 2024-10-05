        int numDigits = String.valueOf(x).length();
        shift = shift % numDigits;
        if (shift == 0) return String.valueOf(x);
        String str = String.valueOf(x);
        return str.substring(shift) + str.substring(0, shift);
    }
}