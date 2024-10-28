        String s = x + "";
        StringBuilder result = new StringBuilder();
        int len = s.length();
        int shift_mod = shift % len;
        if (shift_mod == 0) shift_mod = len;
        for (int i = 0; i < len; i++) {
            if (i >= shift_mod) {
                result.append(s.charAt(i - shift_mod));
            } else {
                result.append(s.charAt(i + len - shift_mod));
            }
        }
        return result.toString();
    }
}

