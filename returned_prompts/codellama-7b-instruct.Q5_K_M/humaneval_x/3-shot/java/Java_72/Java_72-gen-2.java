        if (q.size() == 0) return false;
        if (q.size() == 1) return q.get(0) <= w;

        int sum = 0;
        for (Integer i : q) sum += i;

        if (sum > w) return false;

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < q.size(); i++) {
            int current = 0;
            for (int j = i; j < q.size(); j++) {
                current += q.get(j);
                if (current < min) min = current;
            }
        }
        return min <= w;
    }
}

