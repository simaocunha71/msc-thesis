    public int howManyTimes(String string, String substring) {
        if(string.length() < substring.length()) {
            return 0;
        }
        int count = 0;
        int start = 0;
        while(start < string.length()) {
            if(string.startsWith(substring, start)) {
                count++;
                start += substring.length();
            } else {
                start++;
            }
        }
        return count;
    }
}
