        if (lst.size() == 1) {
            return true;
        }
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < lst.get(i - 1)) {
                return false;
            }
        }
        return true;
    }
}

