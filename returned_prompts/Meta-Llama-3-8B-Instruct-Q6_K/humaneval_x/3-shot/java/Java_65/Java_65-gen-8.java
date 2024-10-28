        String s = String.valueOf(x);
        shift = shift % s.length();
        return s.substring(shift) + s.substring(0, shift);
    }
}

