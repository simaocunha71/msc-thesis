        if (lst.size() == 1) {
            return true;
        }

        for (int i = 0; i < lst.size() - 1; i++) {
            if (lst.get(i) >= lst.get(i + 1)) {
                return false;
            }
        }
        return true;
    }
}

