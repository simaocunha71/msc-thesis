        if (value.charAt(0) == '-') {
            return -countUpper(value.substring(1));
        }
        int res = 0;
        int i = 0;
        while (i < value.length() && value.charAt(i) != '.') {
            res = res * 10 + (value.charAt(i) - '0');
            i += 1;
        }
        int multiplier = 10;
        while (i < value.length()) {
            res += multiplier * (value.charAt(i) - '0');
            multiplier *= 10;
            i += 1;
        }
        if (value.length() > i + 1 && value.charAt(i + 1) != '.') {
            res += multiplier * (value.charAt(i + 1) - '0');
        }
        return res;
    }
}

