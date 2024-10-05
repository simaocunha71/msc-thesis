        String s = Integer.toBinaryString(N);
        int sum = 0;
        for(int i = 0; i < s.length(); i++) {
            sum += s.charAt(i) - '0';
        }
        if(sum == 1) {
            return "1";
        }
        if(sum == 2) {
            return "10";
        }
        if(sum == 3) {
            return "11";
        }
        if(sum == 4) {
            return "100";
        }
        if(sum == 5) {
            return "101";
        }
        if(sum == 6) {
            return "110";
        }
        if(sum == 7) {
            return "111";
        }
        if(sum == 8) {
            return "1000";
        }
        if(sum == 9) {
            return "1001";
        }
        if(sum == 10) {
            return "1010";
        }
        if(sum == 11) {
            return "1011";
        }
        if(sum == 12) {
            return "1100";
        }
        if(sum == 13) {
            return "1101";
        }
        if(sum == 14) {
            return "1110";
        }
        if(sum == 15) {
            return "1111";
        }
        return "";
    }
}
























































































































