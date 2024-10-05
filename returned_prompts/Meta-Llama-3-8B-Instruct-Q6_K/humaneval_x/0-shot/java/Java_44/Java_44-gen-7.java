public String changeBase(int x, int base) {
    if (x < base) {
        return Integer.toString(x);
    }

    String result = "";
    while (x > 0) {
        int remainder = x % base;
        result = remainder + result;
        x = x / base;
    }
    return result;
}
