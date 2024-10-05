        if (q.size() == 0) return false;
        if (q.size() == 1) return q.get(0) <= w;

        int sum = 0;
        int max = q.get(0);
        for (int i = 1; i < q.size(); i++) {
            sum += q.get(i);
            max = Math.max(max, q.get(i));
        }

        return sum <= w && max <= w;
    }
}

