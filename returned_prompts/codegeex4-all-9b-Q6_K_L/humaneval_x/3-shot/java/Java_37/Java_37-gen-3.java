        List<Integer> even = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            even.add(l.get(i));
        }
        Collections.sort(even);
        for (int i = 0; i < l.size(); i += 2) {
            l.set(i, even.get(i / 2));
        }
        return l;
    }
}

