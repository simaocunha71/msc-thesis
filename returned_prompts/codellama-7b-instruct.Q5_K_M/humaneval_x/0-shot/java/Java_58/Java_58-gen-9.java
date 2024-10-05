        for (Integer i: l1) {
            for (Integer j: l2) {
                if (i.equals(j)) {
                    continue A;
                }
            }
            l2.add(i);
        }
        Collections.sort(l2);
        return l2;
    }
}
