        for (int i = lst.size() - 1; i >= 0; i--) {
            for (int j = i + 1; j < lst.size(); j++) {
                if (lst.get(i) == lst.get(j)) {
                    continue A;
                }
            }
            if (lst.get(i) >= i) {
                return lst.get(i);
            }
        }
        return -1;
    }
}

