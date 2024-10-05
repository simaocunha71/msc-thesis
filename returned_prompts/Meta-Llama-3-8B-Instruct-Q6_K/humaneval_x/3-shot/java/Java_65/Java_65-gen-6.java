        int n = Integer.toString(x).length();
        shift = shift % n;
        if (shift == 0) return Integer.toString(x);
        String s = Integer.toString(x);
        return s.substring(shift) + s.substring(0, shift);
    }
}

