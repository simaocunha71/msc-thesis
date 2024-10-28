        if (lst.size() < 2) return true;
        if (lst.size() == 2) return lst.get(0) < lst.get(1);
        if (lst.size() > 2) {
            for (int i = 0; i < lst.size() - 1; i++) {
                if (lst.get(i) > lst.get(i + 1)) return false;
            }
        }
        return true;
    }
}

