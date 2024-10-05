        int n = l.size();
        for (int i = 1; i < n; i++) {
            if (l.get(i) == l.get(i-1)) continue;
            if (l.get(i) > l.get(i-1)) {
                for (int j = i; j < n; j++) {
                    if (l.get(j) < l.get(j-1)) {
                        continue A;
                    }
                }
            } else {
                for (int j = i; j < n; j++) {
                    if (l.get(j) > l.get(j-1)) {
                        continue A;
                    }
                }
            }
            return false;
        }
        return true;
    }
}
