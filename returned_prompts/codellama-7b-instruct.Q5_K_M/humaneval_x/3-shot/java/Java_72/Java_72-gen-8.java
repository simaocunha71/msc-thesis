        if (q.size() == 1) {
            return true;
        } else if (q.size() == 2) {
            if (q.get(0) + q.get(1) <= w) {
                return true;
            }
        } else {
            for (int i = 0; i < q.size() - 2; i++) {
                if (q.get(i) == q.get(q.size() - 1 - i)) {
                    int sum = q.get(i) + q.get(q.size() - 1 - i);
                    if (sum <= w) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}

