        if (l.size() <= 1) return true;

        int inc = 0;
        int dec = 0;

        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) > l.get(i - 1)) inc++;
            if (l.get(i) < l.get(i - 1)) dec++;
        }

        if (inc == l.size() - 1 || dec == l.size() - 1) return true;
        if (inc == 0 || dec == 0) return false;

        return false;
    }
}

