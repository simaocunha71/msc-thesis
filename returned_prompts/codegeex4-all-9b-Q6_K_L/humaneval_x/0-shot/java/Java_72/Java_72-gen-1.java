public boolean willItFly(List<Integer> q, int w) {
    int sum = 0;
    for (int i : q) {
        if (i >= w) {
            return false;
        }
        sum += i;
    }
    return sum <= w;
}