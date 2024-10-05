        for (int i = 0; i < l1.size(); i++) {
            for (int j = 0; j < l2.size(); j++) {
                if (l1.get(i) == l2.get(j)) {
                    break A;
                }
            }
            l1.remove(i);
        }

        Collections.sort(l1);
        return l1;
    }
}