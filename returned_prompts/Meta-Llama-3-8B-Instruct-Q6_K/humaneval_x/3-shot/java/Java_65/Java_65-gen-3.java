        String str = String.valueOf(x);
        int n = str.length();
        if (shift >= n) shift = shift % n;
        return str.substring(shift) + str.substring(0, shift);
    }
}

