        int sum = 0;
        int len = q.size();
        for (int i = 0; i < len; i++) {
            sum += q.get(i);
        }
        return (sum <= w) && (q.get(0) == q.get(len - 1));
    }
}

