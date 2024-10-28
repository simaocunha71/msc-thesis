        for (Integer i : l1) {
            for (Integer j : l2) {
                if (i.equals(j)) {
                    l2.remove(j);
                    continue A;
                }
            }
        }
        return l1;
    }
}
