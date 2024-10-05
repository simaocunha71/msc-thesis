        List<Integer> even = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            even.add(l.get(i));
        }
        Collections.sort(even);
        int index = 0;

        for (int i = 0; i < l.size(); i += 2) {
            l.set(i, even.get(index));
            index += 1;
        }
        return l;
    }
}

