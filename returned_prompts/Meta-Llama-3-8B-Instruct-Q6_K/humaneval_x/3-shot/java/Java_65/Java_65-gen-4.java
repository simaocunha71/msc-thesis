        String s = String.valueOf(x);
        if (shift > s.length()) {
            shift = shift % s.length();
        }
        return s.substring(shift) + s.substring(0, shift);
    }
}

