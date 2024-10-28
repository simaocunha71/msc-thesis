        int n = arr.size();
        if (n == 0) return true;

        int min = 0;
        for (int i = 1; i < n; i++) {
            if (arr.get(i) < arr.get(min)) {
                min = i;
            }
        }

        if (min > 0) {
            return false;
        }

        return true;
    }
}

