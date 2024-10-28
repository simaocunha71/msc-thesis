        int n = arr.size();
        if (n == 0) return true;

        int min = arr.get(0);
        for (int i = 1; i < n; i++) {
            if (arr.get(i) < min) {
                return false;
            }
        }
        return true;
    }
}

