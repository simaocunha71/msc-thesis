        int max = -1;
        for (int i = 0; i < lst.size(); i++) {
            int curr = lst.get(i);
            if (curr > max && curr > 1) {
                max = curr;
            }
        }
        if (max == -1) return -1;

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) >= max) {
                return lst.get(i);
            }
        }
        return -1;

    }
}

