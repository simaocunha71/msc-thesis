    public boolean primeLength(String string) {
        int len = string.length();
        if (len <= 1) {
            return false;
        }
        if (len == 2) {
            return true;
        }
        for (int i = 3; i * i <= len; i += 2) {
            if (len % i == 0) {
                return false;
            }
        }
        return true;
    }
}