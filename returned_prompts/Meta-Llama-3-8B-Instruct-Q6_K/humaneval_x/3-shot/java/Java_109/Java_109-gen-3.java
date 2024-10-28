        int n = arr.size();
        if (n == 0) return true;
        int max = arr.get(0);
        for (int i = 1; i < n; i++) {
            if (arr.get(i) < max) return false;
            max = arr.get(i);
        }
        return true;
    }
}

