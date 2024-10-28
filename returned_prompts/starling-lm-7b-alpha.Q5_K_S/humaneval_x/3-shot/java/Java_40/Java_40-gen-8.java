        Set<Integer> s = new HashSet<>();
        for (int i = 0; i < l.size(); i++) {
            s.add(l.get(i));
            for (int j = 0; j < i; j++) {
                s.add(l.get(i) + l.get(j));
                for (int k = 0; k < j; k++) {
                    if (s.contains(-l.get(i) - l.get(j) - l.get(k))) return true;
                }
            }
        }
        return false;
    }
}

