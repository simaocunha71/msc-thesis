        if (l.size() < 2) return true;

        int diff = l.get(1) - l.get(0);
        for (int i = 2; i < l.size(); i++) {
            if ((l.get(i) - l.get(i - 1)) * diff < 0) return false;
            diff = l.get(i) - l.get(i - 1);
        }
        return true;
     }
}

