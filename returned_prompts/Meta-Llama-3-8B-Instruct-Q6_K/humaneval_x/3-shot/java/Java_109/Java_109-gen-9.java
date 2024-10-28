        int n = arr.size();
        if (n == 0) {
            return true;
        }

        int min = arr.get(0);
        int pos = 0;

        for (int i = 1; i < n; i++) {
            if (arr.get(i) < min) {
                min = arr.get(i);
                pos = i;
            }
        }

        if (pos > 0) {
            return false;
        }

        return true;
    }
}

