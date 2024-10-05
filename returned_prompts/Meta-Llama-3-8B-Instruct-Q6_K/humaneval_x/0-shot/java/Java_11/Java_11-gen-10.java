        String result = "";
        int len = Math.max(a.length(), b.length());
        for (int i = 0; i < len; i++) {
            int bitA = i < a.length() ? a.charAt(i) - '0' : 0;
            int bitB = i < b.length() ? b.charAt(i) - '0' : 0;
            result += (bitA ^ bitB) == 1 ? "1" : "0";
        }
        return result;
    }
}
