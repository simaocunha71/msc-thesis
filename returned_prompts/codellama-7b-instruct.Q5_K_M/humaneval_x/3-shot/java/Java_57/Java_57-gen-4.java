        if (l.size() <= 1) return true;
        int inc = 1;
        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) > l.get(i - 1)) inc = 1;
            else if (l.get(i) < l.get(i - 1)) inc = -1;
            else continue;

            for (int j = i + 1; j < l.size(); j++) {
                if ((l.get(j) > l.get(j - 1) && inc == 1) || (l.get(j) < l.get(j - 1) && inc == -1)) return false;
            }
        }
        return true;
    }
}

