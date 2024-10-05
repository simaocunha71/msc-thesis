public String changeBase(int x, int base) {
    StringBuilder sb = new StringBuilder();
    while (x > 0) {
        x = x % base;
        if (x >= 10) {
            sb.insert(0, (char) ('A' + x - 10));
        } else {
            sb.insert(0, x);
        }
        x = x / base;
    }
    return sb.toString();
}