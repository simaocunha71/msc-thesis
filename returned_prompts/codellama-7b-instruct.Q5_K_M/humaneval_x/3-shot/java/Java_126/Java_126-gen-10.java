        if (lst.size() == 1) {
            return true;
        } else if (lst.size() == 0) {
            return false;
        }

        boolean is_sorted = true;
        boolean has_duplicate = false;

        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < lst.get(i - 1)) {
                is_sorted = false;
            }
            if (lst.get(i) == lst.get(i - 1)) {
                has_duplicate = true;
            }
        }
        return is_sorted && !has_duplicate;
    }
}

