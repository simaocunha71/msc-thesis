        int sum = 0;
        for (int i : q) {
            sum += i;
        }

        if (sum > w) {
            return false;
        }

        for (int i = 0; i < q.size() / 2; i++) {
            if (q.get(i) != q.get(q.size() - i - 1)) {
                return false;
            }
        }

        return true;
    }
}

