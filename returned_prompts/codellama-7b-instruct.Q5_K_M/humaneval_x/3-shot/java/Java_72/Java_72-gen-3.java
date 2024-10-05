        if (q.size() == 1) {
            return true;
        }
        int sum = 0;
        for (int i : q) {
            sum += i;
        }
        if (sum > w) {
            return false;
        }
        if (sum == w) {
            return true;
        }
        boolean isPalindrom = true;
        for (int i = 0; i < q.size() / 2; i++) {
            if (q.get(i) != q.get(q.size() - 1 - i)) {
                isPalindrom = false;
                break;
            }
        }
        if (isPalindrom) {
            return true;
        }
        return false;
    }
}

