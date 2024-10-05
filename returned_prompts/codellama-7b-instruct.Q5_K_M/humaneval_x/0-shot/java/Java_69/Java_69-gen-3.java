        for (int i = 1; i <= lst.size(); i++) {
            int count = 0;
            for (int j = 0; j < lst.size(); j++) {
                if (lst.get(j) == i) {
                    count++;
                }
            }
            if (count >= i) {
                return i;
            }
        }
        return -1;
    }
}
