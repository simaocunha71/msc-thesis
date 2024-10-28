        int n = l.size();
        if (n == 1) return true;

        int inc = 1, dec = -1, same = 0;
        for (int i = 1; i < n; i++) {
            if (l.get(i - 1) < l.get(i)) inc = 1;
            if (l.get(i - 1) > l.get(i)) dec = -1;
            if (l.get(i - 1) == l.get(i)) same = 1;
        }
        return (inc == 1 || dec == -1 || same == 1);
    }
}

