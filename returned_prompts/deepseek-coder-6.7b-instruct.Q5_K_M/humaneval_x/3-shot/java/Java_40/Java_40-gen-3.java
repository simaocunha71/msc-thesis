        int n = l.size();
        if (n < 3) return false;

        Collections.sort(l);

        for (int i = 0; i < n - 1; i++) {
            int left = i + 1;
            int right = n - 1;
            int x = l.get(i);
            while (left < right) {
                if (x + l.get(left) + l.get(right) == 0) {
                    return true;
                } else if (x + l.get(left) + l.get(right) < 0) {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }
        return false;
    }
}

