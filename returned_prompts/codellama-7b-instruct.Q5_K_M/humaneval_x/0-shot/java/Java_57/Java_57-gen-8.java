        int n = l.size();
        if (n <= 1)
            return true;
        int prev = l.get(0);
        for (int i = 1; i < n; i++) {
            int curr = l.get(i);
            if (prev > curr) {
                // decreasing
                for (int j = i + 1; j < n; j++) {
                    if (l.get(j) < prev)
                        continue A;
                }
                return true;
            }
            else if (prev < curr) {
                // increasing
                for (int j = i + 1; j < n; j++) {
                    if (l.get(j) > prev)
                        continue A;
                }
                return true;
            }
            prev = curr;
        }

        return false;
    }
}
