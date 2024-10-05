        int max = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) > max) {
                max = lst.get(i);
            }
        }
        return max;
    }
}
