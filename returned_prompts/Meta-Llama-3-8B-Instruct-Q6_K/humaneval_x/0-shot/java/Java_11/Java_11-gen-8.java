        int len = a.length();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < len; i++) {
            char ca = a.charAt(i);
            char cb = b.charAt(i);
            if(ca == '0' && cb == '0') {
                sb.append('0');
            } else if(ca == '1' && cb == '1') {
                sb.append('0');
            } else {
                sb.append('1');
            }
        }
        return sb.toString();
    }
}
