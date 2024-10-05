        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) < l.get(i - 1)) return false;
        }
        return true;
    }
}
