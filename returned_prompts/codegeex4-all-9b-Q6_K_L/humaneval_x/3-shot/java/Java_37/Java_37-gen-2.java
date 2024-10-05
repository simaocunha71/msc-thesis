        List<Integer> even = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            even.add(l.get(i));
        }
        Collections.sort(even);
        for (int i = 0; i < even.size(); i++) {
            l.set(2 * i, even.get(i));
        }
        return l;
    }
}

