        List<Integer> even_indices = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            even_indices.add(l.get(i));
        }
        Collections.sort(even_indices);

        for (int i = 0; i < l.size(); i += 2) {
            l.set(i, even_indices.remove(0));
        }
        return l;
    }
}

