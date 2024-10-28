public boolean willItFly(List<Integer> q, int w) {
    return q.stream().reduce(Integer::sum).orElse(0) <= w && isPalindrome(q);
}

private boolean isPalindrome(List<Integer> q) {
    int start = 0;
    int end = q.size() - 1;

    while (start < end) {
        if (!q.get(start).equals(q.get(end))) {
            return false;
        }
        start++;
        end--;
    }

    return true;
}