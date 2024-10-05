        List<Integer> l2 = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                l2.add(l.get(i));
            }
        }
        Collections.sort(l2);
        int index = 0;
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                l.set(i, l2.get(index));
                index += 1;
            }
        }
        return l;
    }
}

