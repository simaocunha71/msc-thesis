        if (q.size() == 0) return false;
        if (q.size() == 1) return true;
        if (q.size() == 2) return q.get(0) + q.get(1) <= w;

        boolean balanced = true;
        int sum = 0;
        for (int i = 0; i < q.size() / 2; i++) {
            if (q.get(i) != q.get(q.size() - i - 1)) {
                balanced = false;
                break;
            }
            sum += q.get(i);
        }
        if (balanced) {
            if (sum <= w) return true;
        }
        return false;
    }
}

