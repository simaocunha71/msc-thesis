public String changeBase(int x, int base) {
    String[] digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"};
    StringBuilder sb = new StringBuilder();
    while (x > 0) {
        sb.insert(0, digits[x % base]);
        x /= base;
    }
    return sb.toString();
}
