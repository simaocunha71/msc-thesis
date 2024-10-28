        if (q.size() == 1) {
            return q.get(0) <= w;
        }

        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }

        if (sum > w) {
            return false;
        }

        for (int i = 0; i < q.size(); i++) {
            if (q.get(i) != q.get(q.size() - 1 - i)) {
                return false;
            }
        }

        return true;
    }
}

