        int n = l.size();
        if (n < 3)
            return false;

        Collections.sort(l);

        for (int i = 0; i < n - 1; i++) {
            int a = l.get(i);
            int start = i + 1;
            int end = n - 1;
            while (start < end) {
                if (a + l.get(start) + l.get(end) == 0) {
                    return true;
                }
                else if (a + l.get(start) + l.get(end) < 0) {
                    start += 1;
                }
                else {
                    end -= 1;
                }
            }
        }
        return false;
    }
}

