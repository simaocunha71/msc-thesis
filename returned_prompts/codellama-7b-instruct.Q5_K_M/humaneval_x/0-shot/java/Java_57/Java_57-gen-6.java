        if (l.size() == 1) return true;
        int inc = 1;
        int dec = -1;
        int n = l.size();
        for (int i = 0; i < n - 1; i++) {
            if (l.get(i) > l.get(i + 1)) inc = 0;
            if (l.get(i) < l.get(i + 1)) dec = 0;
            if (inc == 0 && dec == 0) return false;
        }
        return true;
    }
}

